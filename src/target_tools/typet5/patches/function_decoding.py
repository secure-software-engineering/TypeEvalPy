import asyncio
import copy
import random
import warnings

import torch

from .data import CtxArgs, src_to_chunks
from .function_dataset import (
    SignatureMap,
    ctx_modules_for_elem,
    mk_preamble,
    reformat_elems,
    wrap_main_code,
)
from .model import DatasetPredResult, ModelWrapper
from .static_analysis import (
    ElemSignature,
    FunctionSignature,
    ModuleName,
    ModulePath,
    ProjectPath,
    PythonElem,
    PythonFunction,
    PythonProject,
    PythonVariable,
    SignatureErrorAnalysis,
    UsageAnalysis,
    VariableSignature,
    reorder_signature_map,
)
from .tokenized_src import PreprocessArgs, TokenSeq, tokenized_src_from_segs
from .type_check import PythonType, parse_type_str
from .type_env import AccuracyMetric, AnnotPath, collect_user_annotations
from .utils import *


@dataclass
class RolloutPrediction:
    """Record the information generated during a decoding rollout.

    - final_sigmap: The final type assignments for each element.
    - predicted_sigmap: The type assignments predicted by the model,
    immediately before modified by the oracle (if any). This will be identical
    to final_sigmap if no oracle is used.
    - elem2inputs: Maps each element to the corresponding input fed to the model.
    - elem2preds: Maps each element to the corresponding types predicted by
    the model.
    """

    assignments: SignatureMap
    elem2preds: dict[ProjectPath, Sequence[PythonType]]
    elem2inputs: dict[ProjectPath, dict]
    elem2location: dict[ProjectPath, dict]
    pred_assignments: SignatureMap = field(default_factory=SignatureMap)

    @property
    def final_sigmap(self) -> SignatureMap:
        return self.assignments

    @property
    def predicted_sigmap(self) -> SignatureMap:
        if hasattr(self, "pred_assignments") and self.pred_assignments:
            return self.pred_assignments
        else:
            return self.assignments


@dataclass
class EvalResult:
    project_roots: list[Path]
    predictions: list[RolloutPrediction]
    label_maps: list[SignatureMap]

    def error_analysis(
        self,
        project: int | str | None,
        metric: AccuracyMetric,
    ) -> SignatureErrorAnalysis:
        projects = self.find_projects(project)

        label_maps = dict[str, SignatureMap]()
        pred_maps = dict[str, SignatureMap]()

        for i in projects:
            pname = self.project_roots[i].name
            label_maps[pname] = self.label_maps[i]
            pred_maps[pname] = self.predictions[i].predicted_sigmap

        return SignatureErrorAnalysis(
            pred_maps,
            label_maps,
            metric,
            error_on_mismatched_signature=True,  # there shouldn't be any mismatch
        )

    def find_projects(self, identifier: int | str | None) -> list[int]:
        if isinstance(identifier, int):
            projects = [identifier]
        elif isinstance(identifier, str):
            projects = [
                i for i, p in enumerate(self.project_roots) if p.name == identifier
            ]
            assert projects, f"Project not found: {identifier}"
        else:
            projects = list(range(len(self.predictions)))
        return projects

    def inspect_elem(self, identifier: int | str | None, path: ProjectPath) -> None:
        pid = self.find_projects(identifier)[0]

        print("Expected: ", self.label_maps[pid][path])
        print("Predicted:", self.predictions[pid].final_sigmap[path])
        print("Code:")
        print(decode_tokens(self.predictions[pid].elem2inputs[path]["input_ids"]))

    def print_predictions(self, write=False) -> None:
        def merge_sigmap_with_elem2location(predicted_sigmap, elem2location):
            merged_sigmap = {}
            for path, signature in predicted_sigmap.items():
                if path in elem2location:
                    location = elem2location[path]
                    merged_sigmap[path] = f"{str(signature)} - Location: {location}"
                else:
                    merged_sigmap[path] = str(signature)

            return merged_sigmap

        for proj, rollout, label_map in zip(
            self.project_roots, self.predictions, self.label_maps
        ):
            sig_map = reorder_signature_map(rollout.predicted_sigmap, label_map)
            merged_sigmap = merge_sigmap_with_elem2location(
                sig_map, rollout.elem2location
            )
            print("=" * 20, proj, "=" * 20)
            for path, sig in merged_sigmap.items():
                print(f"\t{path}: {str(sig)}")
                if write:
                    parts = str(path).split("/")
                    folder_path = proj
                    for part in parts[:-1]:
                        part = part.replace(".", "/")
                        folder_path /= f"{part}.txt"
                    with open(folder_path, "a") as file:
                        file.write(f"{parts[1]}:{str(sig)}\n")


@dataclass
class RolloutCtx:
    model: ModelWrapper

    async def evaluate_on_projects(
        self,
        projects: Sequence[PythonProject],
        pre_args: PreprocessArgs,
        decode_order: "DecodingOrder",
        concurrency: int = DefaultWorkers,
        use_oracle: bool = False,
        tqdm_args: dict = {},
    ) -> EvalResult:
        """Evaluate the model's prediction accuracy on a given set of projects, masking
        any existing type annotations and treating them as the ground truth.
        Note that the model does make predictions for those places with a missing type
        annotation, but they are not counted in the accuracy computation (and only serve as
        an intermediate for information propogation).

        Args:
        - use_oracle: If True, the model's predictions are immediately replaced by the
        ground truth type annotations before moving on to the next element. This simulates
        an interactive setting where the user corrects the model's incorrect predictions.
        """
        if pre_args.drop_env_types and decode_order.types_in_ctx():
            warnings.warn(
                "The decoding order contains types in context, but drop_env_types=True in the pre-processing args."
            )

        n_total_elems = sum(1 for p in projects for e in p.all_elems())
        project_roots = [p.root_dir for p in projects]
        rollouts: list[Any] = [None for _ in projects]
        label_maps: list[Any] = [dict() for _ in projects]
        with tqdm(
            total=decode_order.traverse_length(n_total_elems),
            desc="evaluate_on_projects",
            smoothing=0.01,
            **tqdm_args,
        ) as pbar, ThreadPoolExecutor(1) as model_executor, ProcessPoolExecutor(
            concurrency
        ) as cpu_executor:

            async def eval_project(id_project: tuple[int, PythonProject]):
                id, project = id_project
                label_sigs = project.get_sigmap()
                label_maps[id] = label_sigs
                oracle = label_sigs if use_oracle else None
                r = await self.project_rollout(
                    project.mask_types(),
                    pre_args,
                    decode_order,
                    cpu_executor=cpu_executor,
                    model_executor=model_executor,
                    oracle=oracle,
                    progress_cbk=lambda e, p, s: pbar.update(),
                )
                rollouts[id] = r

            await throttled_async_run(
                eval_project, list(enumerate(projects)), concurrency=concurrency
            )

        return EvalResult(project_roots, rollouts, label_maps)

    async def run_on_project(
        self,
        project: PythonProject,
        pre_args: PreprocessArgs,
        decode_order: "DecodingOrder",
        concurrency: int = DefaultWorkers,
    ):
        sigmap = dict[ProjectPath, ElemSignature]()

        def callback(e: PythonElem, types, sig: ElemSignature) -> None:
            if e.path not in sigmap:
                sigmap[e.path] = sig
                print(f"{e.path}: {str(sig)}")
            else:
                old_sig = sigmap[e.path]
                corrected = str(old_sig) != str(sig)
                sigmap[e.path] = sig
                if corrected:
                    print(f"(updated) {e.path}: {str(sig)}")

        with ThreadPoolExecutor(1) as model_executor, ProcessPoolExecutor(
            concurrency
        ) as cpu_executor:
            return await self.project_rollout(
                project,
                pre_args,
                decode_order,
                cpu_executor=cpu_executor,
                model_executor=model_executor,
                oracle=None,
                progress_cbk=callback,
            )

    async def project_rollout(
        self,
        project: PythonProject,
        pre_args: PreprocessArgs,
        decode_order: "DecodingOrder",
        cpu_executor: ProcessPoolExecutor,
        model_executor: ThreadPoolExecutor,
        oracle: SignatureMap | None = None,
        progress_cbk: Callable[
            [PythonElem, Sequence[PythonType], ElemSignature], Any
        ] = lambda x, y, z: None,
    ) -> RolloutPrediction:
        """Note: when evaluating on dataset with ground truth labels, we need to
        first replace all labels with `SpecialNames.TypeMask` before feeding to
        this function.
        """
        # Model executor needs to be single threaded.
        assert_eq(model_executor._max_workers, 1)

        eloop = asyncio.get_event_loop()
        analysis: UsageAnalysis = await eloop.run_in_executor(
            cpu_executor,
            UsageAnalysis,
            project,
            pre_args.add_override_usages,
            pre_args.add_implicit_rel_imports,
        )
        to_visit = [analysis.path2elem[p] for p in decode_order.traverse(analysis)]
        visit_set = {e.path for e in to_visit}
        for e in project.all_elems():
            assert e.path in visit_set, f"{e.path} not in the decoder order."
        preamble_cache = dict[ModuleName, tuple[str, TokenSeq]]()

        pred_sigmap = SignatureMap()
        final_sigmap = SignatureMap()
        elem2location = dict[ProjectPath, dict]()
        elem2preds = dict[ProjectPath, Sequence[PythonType]]()
        elem2inputs = dict[ProjectPath, dict]()
        mask_annot = cst.Annotation(cst.Name(SpecialNames.TypeMask))

        # Parallelize computation between dependency-free elements
        for elem in to_visit:
            # fetch line number of element
            elem_path = str(elem).split("=")[1]
            module, path = elem_path.strip(")").split("/")
            project_path = ProjectPath(
                module,
                path,
            )
            code_range_output = project.get_elem_location(project_path)
            line_value = code_range_output[1].start.line
            # construct input for the model
            # first, create or retrieve the preamble
            cur_module = elem.path.module
            if cur_module not in preamble_cache:
                preamble_tuple = await eloop.run_in_executor(
                    cpu_executor,
                    mk_preamble,
                    project.modules[cur_module].tree,
                    pre_args,
                )
                preamble_cache[cur_module] = preamble_tuple
            preamble, tokenized_preamble = preamble_cache[cur_module]

            # then, make all missing types in the signature a prediction target
            if isinstance(elem, PythonVariable):
                sig = elem.get_signature()
                elem_sig = copy.deepcopy(sig)
                if sig.annot is None:
                    elem_sig.annot = mask_annot
                elem_map = {elem.path: elem_sig}
            elif isinstance(elem, PythonFunction):
                sig = elem.get_signature()
                elem_sig = copy.deepcopy(sig)
                for n, a in elem_sig.params.items():
                    if a is None:
                        elem_sig.params[n] = mask_annot
                if elem_sig.returns is None:
                    elem_sig.returns = mask_annot
                elem_map = {elem.path: elem_sig}
            else:
                raise NotImplemented(f"Unsupported element type {type(elem)}")
            # inline the type signatures using `reformat_elems`
            main_lines = reformat_elems(
                [elem],
                analysis.path2class,
                cast(SignatureMap, elem_map),
                keep_body_types=True,
            )

            left_m, right_m = ctx_modules_for_elem(
                elem,
                analysis,
                pre_args,
                final_sigmap if decode_order.types_in_ctx() else {},
            )

            model_inputs = await eloop.run_in_executor(
                cpu_executor,
                construct_model_inputs,
                cst.Module(main_lines),
                left_m,
                right_m,
                preamble,
                tokenized_preamble,
                self.model.args.ctx_args,
            )

            pred_types = list[PythonType]()
            new_sig = copy.deepcopy(sig)
            if model_inputs:
                for chunk in model_inputs:
                    chunk = {
                        "input_ids": torch.tensor([chunk["input_ids"]]),
                        "labels": torch.tensor([chunk["labels"]]),
                        "n_labels": torch.tensor([chunk["n_labels"]]),
                    }
                    preds, _ = await eloop.run_in_executor(
                        model_executor, self.model.predict_on_batch, chunk
                    )
                    pred_types.extend(preds[0])
                elem2inputs[elem.path] = model_inputs[0]

                # update the signature with the predicted types
                if isinstance(new_sig, VariableSignature):
                    assert new_sig.annot is None or is_mask_annot(
                        new_sig.annot
                    ), f"For {elem}, sig={new_sig}"
                    assert_eq(len(pred_types), 1)
                    new_sig.annot = cst.Annotation(
                        cst.parse_expression(str(pred_types[0]))
                    )
                elif isinstance(elem, PythonFunction):
                    # assert len(pred_types) >= len(sig.params) + 1
                    n_pred = 0
                    for n, a in new_sig.params.items():
                        if a is None or is_mask_annot(a):
                            new_type = cst.parse_expression(str(pred_types[n_pred]))
                            new_sig.params[n] = cst.Annotation(new_type)
                            n_pred += 1
                    if new_sig.returns is None or is_mask_annot(new_sig.returns):
                        new_sig.returns = cst.Annotation(
                            cst.parse_expression(str(pred_types[n_pred]))
                        )
                pred_sigmap[elem.path] = new_sig
            if (
                oracle is not None
                and (label := oracle.get(elem.path)) is not None
                and type(label) == type(new_sig)
            ):
                new_sig = new_sig.updated(as_any(label))
            final_sigmap[elem.path] = new_sig
            elem2preds[elem.path] = pred_types
            elem2location[elem.path] = line_value
            if model_inputs:
                progress_cbk(elem, pred_types, new_sig)

        return RolloutPrediction(
            final_sigmap, elem2preds, elem2inputs, elem2location, pred_sigmap
        )


def is_mask_annot(a: cst.Annotation) -> bool:
    match a.annotation:
        case cst.Name(value=SpecialNames.TypeMask):
            return True
    return False


class DecodingOrder(ABC):
    @abstractmethod
    def traverse(self, analysis: UsageAnalysis) -> list[ProjectPath]:
        ...

    def traverse_length(self, n_elems: int) -> int:
        return n_elems

    def types_in_ctx(self) -> bool:
        return True


class DecodingOrders:
    class IndependentOrder(DecodingOrder):
        """Decode each element independently: the types predicted by the model will
        not be added to the context for later elements"""

        @staticmethod
        def traverse(analysis: UsageAnalysis) -> list[ProjectPath]:
            return [e.path for e in analysis.project.all_elems()]

        @staticmethod
        def types_in_ctx() -> bool:
            return False

    class RandomOrder(DecodingOrder):
        "Visit all elements once in a random order."

        @staticmethod
        def traverse(analysis: UsageAnalysis) -> list[ProjectPath]:
            elems = [e.path for e in analysis.project.all_elems()]
            random.shuffle(elems)
            return elems

    class Caller2Callee(DecodingOrder):
        """Visit the callers first before visiting the callees. The order among
        elements in a dependency cycle is arbitrary."""

        @staticmethod
        def traverse(analysis: UsageAnalysis) -> list[ProjectPath]:
            sorted = list[ProjectPath]()
            visited = set[ProjectPath]()

            def visit(p: ProjectPath) -> None:
                if p in visited or p not in analysis.path2elem:
                    return
                visited.add(p)
                for u in analysis.used2user.get(p, []):
                    visit(u.user)
                sorted.append(p)

            for m in reversed(list(analysis.project.all_elems())):
                # start with the latest elements in the project
                visit(m.path)
            return sorted

    class Callee2Caller(DecodingOrder):
        """Visit the callees before visiting the callers. Give the reverse ordering
        of `Caller2Callee`"""

        @staticmethod
        def traverse(analysis: UsageAnalysis) -> list[ProjectPath]:
            return list(reversed(DecodingOrders.Caller2Callee.traverse(analysis)))

    class DoubleTraversal(DecodingOrder):
        """Visit each element twice: `Callee2Caller` followed by `Caller2Callee`."""

        @staticmethod
        def traverse(analysis: UsageAnalysis) -> list[ProjectPath]:
            pass1 = DecodingOrders.Callee2Caller.traverse(analysis)
            pass2 = list(reversed(pass1))
            return pass1 + pass2[1:]

        @staticmethod
        def traverse_length(n_elems: int) -> int:
            return 2 * n_elems - 1

    @dataclass
    class Reversed(DecodingOrder):
        original: DecodingOrder

        def traverse(self, analysis: UsageAnalysis) -> list[ProjectPath]:
            order = self.original.traverse(analysis)
            order.reverse()
            return order

        def traverse_length(self, n_elems: int) -> int:
            return self.original.traverse_length(n_elems)

    class RandomTwice(DecodingOrder):
        """Perform random traversal twice."""

        @staticmethod
        def traverse(analysis: UsageAnalysis) -> list[ProjectPath]:
            pass1 = DecodingOrders.RandomOrder.traverse(analysis)
            pass2 = DecodingOrders.RandomOrder.traverse(analysis)
            return pass1 + pass2

        @staticmethod
        def traverse_length(n_elems: int) -> int:
            return 2 * n_elems


def construct_model_inputs(
    main_mod: cst.Module,
    left_m: cst.Module | None,
    right_m: cst.Module | None,
    preamble: str,
    preamble_tkns: TokenSeq,
    ctx_args: CtxArgs,
) -> list[dict]:
    "Return a list of model inputs."
    main_code_string = wrap_main_code(main_mod.code)
    code_segs = main_code_string.split(SpecialNames.TypeMask)
    n_masks = len(code_segs) - 1

    if n_masks == 0:
        return []

    left_tks = None
    if left_m is not None:
        left_tks = DefaultTokenizer.encode(left_m.code, add_special_tokens=False)
    right_tks = None
    if right_m is not None:
        right_tks = DefaultTokenizer.encode(right_m.code, add_special_tokens=False)

    annots, types = collect_user_annotations(main_mod)

    try:
        src = tokenized_src_from_segs(
            file=Path("[construct_model_inputs]"),
            repo=Path("[construct_model_inputs]"),
            preamble=preamble,
            tokenized_preamble=preamble_tkns,
            code_segs=code_segs,
            types=types,
            types_str=[SpecialNames.TypeMask] * len(annots),
            annots_info=annots,
            cst_code=main_code_string,
            left_extra_tks=left_tks,
            right_extra_tks=right_tks,
        )
    except:
        print(f"{n_masks}, {types=}, {annots=}")
        print("============ Main code string =========")
        print(main_code_string)
        raise
    chunks, _ = src_to_chunks(src, (0, n_masks), ctx_args)
    return chunks
