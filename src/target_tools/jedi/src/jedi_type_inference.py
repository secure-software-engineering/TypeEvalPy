import os
import re
from cmath import exp
from pathlib import Path
from typing import List

import jedi


class TypeInferenceJedi:
    """
    Infer types for the modules accessible from the entrypoints with the help of Jedi
    """

    def __init__(self, name: str, entry_point: str):
        """
        Args:
            name: the name of the type inference analyser
            entry_point: the entry point, can be the root folder of a package or a python file
        """
        self.name = name
        self.entry_point = entry_point
        self.import_graph = None
        self.leaves = []
        self.jedi_output = {}

        # get all Python files in dir
        if os.path.isdir(entry_point):
            self.leaves = sorted(Path(entry_point).rglob("*.py"))
        else:
            self.leaves = [Path(entry_point)]

    def check_ending(self, s):
        return bool(re.search(r"\([a-zA-Z, ]*\)$", s))

    def transform_type_string(self, s: str) -> str:
        if "[" in s:
            # Use regular expression to replace content inside square brackets with empty string
            s = re.sub(r"\[.*\]", "", s)
            # Convert the first letter to lower-case
            s = s[0].lower() + s[1:]
        if s == "None":
            s = "Nonetype"
        return s

    def parse_type_hint(self, type_hint, name):
        # TODO: Replace this with a more sane version from the internals of Jedi
        _type = set()
        if type_hint == f"{name}()":
            pass
        elif type_hint and type_hint.startswith("<lambda>"):
            _type.add("callable")
        elif type_hint:
            try:
                _t = type_hint.split(" -> ")[-1]
                if "Union" in _t:
                    _list_of_types = (
                        _t.split("Union")[1]
                        .replace("[", "")
                        .replace("]", "")
                        .split(", ")
                    )
                    for _l_t in _list_of_types:
                        _type.add(_l_t)
                elif self.check_ending(_t):
                    _type.add("callable")
                else:
                    _t = _t.replace(")", "").replace("(", "")
                    _type.add(_t)
            except Exception as e:
                print("Unable to parse type hint")
                pass

        _type = set([self.transform_type_string(s) for s in _type])
        return _type

    def find_types_by_execute(self, jedi_obj):
        _type = set()
        _try_type_hint = None

        try:
            _try_type_hint = self.parse_type_hint(
                jedi_obj.get_type_hint(), jedi_obj.name
            )
        except Exception as e:
            print("Unable to fetch type hint from Jedi")

        if _try_type_hint and not next(iter(_try_type_hint)).startswith(jedi_obj.name):
            _type = _try_type_hint
        else:
            for _name in jedi_obj.execute():
                _type = self.parse_type_hint(_name.get_type_hint(), _name.name)

                if not _type:
                    # Find builtin types
                    if _name.module_name == "builtins":
                        _type.add(_name.name)

        _type = set([self.transform_type_string(s) for s in _type])
        return _type

    def get_function_name(self, jedi_obj):
        """Return the qualified name of jedi_obj relative to its module,
        walking up parent scopes so nested functions become 'outer.inner'."""
        try:
            if jedi_obj.name == "<lambda>":
                return "lambda"
            parts = []
            current = jedi_obj
            while current is not None and current.type != "module":
                name = "lambda" if current.name == "<lambda>" else current.name
                parts.append(name)
                try:
                    current = current.parent()
                except Exception:
                    break
            return ".".join(reversed(parts)) if parts else jedi_obj.name
        except Exception:
            print("full_name not found in jedi_obj?")
            return jedi_obj.name

    def infer_types(self):
        """
        Infer the types for the modules accessible from the entrypoint
        """
        output_inferred = []

        for node in self.leaves:
            var_names = {}
            # self.code = open(node).read()
            for _name in jedi.Script(path=str(node)).get_names(
                all_scopes=1, definitions=1
            ):
                var_names[f"{_name.name}:{_name.line}_{_name.column}"] = {
                    "line": _name.line,
                    "column": _name.column,
                    "jedi_obj": _name,
                }

            for var, pos in var_names.items():
                # TODO: Should this be really skipped?
                if var.startswith(("self", "__init__")):
                    continue

                # HACK: Currently following a two-step approach to fetch types from Jedi.
                # Typically, we should be able to directly infer on the 'jedi_obj', but
                # there is a performance issue of Script object after a few iterations.
                # Creating new Script obj everytime to mitigate this as suggested by author.
                _infer = jedi.Script(path=str(node)).infer(pos["line"], pos["column"])
                if _infer:
                    for inferred in _infer:
                        if inferred.type == "function":
                            # Distinguish between the function's own definition
                            # site (return-type is what's wanted, e.g. for `def
                            # func1():`) and a reference to it (callable is
                            # what's wanted, e.g. for `a = func1`).
                            at_def_site = (
                                pos["line"] == inferred.line
                                and pos["column"] == inferred.column
                            )

                            if at_def_site:
                                _type = self.find_types_by_execute(inferred)

                                _info = {
                                    "file": node.name,
                                    "line_number": pos["line"],
                                    "col_offset": pos["column"] + 1,
                                }
                                if inferred.name != "<lambda>":
                                    _info["function"] = self.get_function_name(inferred)
                                _info["type"] = _type if _type else {"any"}

                                variable_name = var.split(":")[0].strip()
                                if variable_name != self.get_function_name(inferred):
                                    _info["variable"] = variable_name
                                if _type:
                                    output_inferred.append(_info)
                            else:
                                variable_name = var.split(":")[0].strip()
                                _info = {
                                    "file": node.name,
                                    "line_number": pos["line"],
                                    "col_offset": pos["column"] + 1,
                                    "variable": variable_name,
                                    "type": {"callable"},
                                }
                                parent = pos["jedi_obj"].parent()
                                if parent and parent.type != "module":
                                    parent_func = self.get_function_name(parent)
                                    if parent_func:
                                        _info["function"] = parent_func
                                output_inferred.append(_info)

                        elif inferred.type == "instance":
                            try:
                                _type = inferred.get_type_hint()
                                if _type == inferred.name:
                                    if not inferred.full_name.startswith(
                                        (self.entry_point.stem, "builtins", "typing")
                                    ):
                                        _type = inferred.full_name
                                    else:
                                        _type = _type.lower()

                                _type = self.transform_type_string(_type)
                            except Exception as e:
                                print("Unable to fetch type hint from Jedi")
                                _type = None

                            if not _type:
                                # Find builtin types
                                if inferred.module_name == "builtins":
                                    _type = inferred.name

                            _info = {
                                "file": node.name,
                                "line_number": pos["line"],
                                "col_offset": pos["column"] + 1,
                                "variable": var.split(":")[0],
                                "type": {_type},
                            }
                            parent = pos["jedi_obj"].parent()
                            if parent and parent.type != "module":
                                parent_func = self.get_function_name(parent)
                                if parent_func:
                                    _info["function"] = parent_func
                            if _type:
                                output_inferred.append(_info)

                        elif inferred.type == "param":
                            _type = inferred.get_type_hint()
                            _info = {
                                "file": node.name,
                                "line_number": pos["line"],
                                "col_offset": pos["column"] + 1,
                                "variable": var.split(":")[0],
                                "function": self.get_function_name(
                                    pos["jedi_obj"].parent()
                                ),
                                "type": {_type},
                            }

                            if _type:
                                output_inferred.append(_info)

                        elif inferred.type == "class":
                            pass

                else:
                    if pos["jedi_obj"].type == "param":
                        _type = pos["jedi_obj"].get_type_hint()
                        _info = {
                            "file": node.name,
                            "line_number": pos["line"],
                            "col_offset": pos["column"] + 1,
                            "parameter": var.split(":")[0],
                            "function": self.get_function_name(
                                pos["jedi_obj"].parent()
                            ),
                            "type": {_type if _type else "any"},
                        }

                        output_inferred.append(_info)

            self.output_inferred = output_inferred

    def get_types(self) -> List[dict]:
        """
        Get the inferred type information in a list of dictionaries
        """
        return self.output_inferred


if __name__ == "__main__":
    file_path = Path(
        "/mnt/Projects/PhD/Research/Student-Thesis/4_type_inference_benchmark(Sam)/git_sources/master-thesis-of-samkutty/.scrapy/test.py"
    )
    inferer = TypeInferenceJedi(name=file_path, entry_point=file_path)
    inferer.infer_types()
    inferred = inferer.get_types()
    print(inferred)
