import csv
import json
import logging
import os
import re
from pathlib import Path

logger = logging.getLogger("Result Analysis")

ML_TOOLS = ["type4py", "hityperdl"]
STANDARD_TOOLS = [
    "scalpel",
    "hityper",
    "jedi",
    "pyright",
    "headergen",
]
TOP_N = [1, 3, 5]

TYPE_CATEGORIES = ["function_returns", "function_parameters", "local_variables"]
PYTHON_FEATURES_CATEGORIES = [
    "args",
    "assignments",
    "builtins",
    "classes",
    "decorators",
    "dicts",
    "direct_calls",
    "dynamic",
    "exceptions",
    "external",
    "functions",
    "generators",
    "imports",
    "kwargs",
    "lambdas",
    "lists",
    "mro",
    "returns",
]
SENSITIVITIES_CATEGORIES = [
    "context_sensitivity",
    "field_sensitivity",
    "field_sensitivity_depth_2",
    "field_sensitivity_depth_3",
    "flow_sensitivity",
    "inter_procedural",
    "intra_procedural",
    "object_sensitivity",
    "path_sensitivity",
]


def sort_stats(stats):
    # Sort stats based on total_caught
    stats = {
        k: v
        for k, v in sorted(
            stats.items(),
            key=lambda item: sum(
                sub_dict["total_caught"] for sub_dict in item[1]["exact_match"].values()
            ),
            reverse=True,
        )
    }

    return stats


# TODO: Use translator to avoid fixing this here
def sort_facts(data):
    data = sorted(data, key=lambda x: int(x["line_number"]))
    for fact in data:
        if "type" in fact:
            if isinstance(fact["type"], list):
                fact["type"].sort()
    return data


def categorize_facts(data):
    type_categories = {k: [] for k in TYPE_CATEGORIES}
    others = []
    for fact in data:
        # Function return:
        if ("function" in fact) and not (
            any([x in fact.keys() for x in ["variable", "parameter"]])
        ):
            type_categories["function_returns"].append(fact)

        # Function parameters
        elif all([x in fact.keys() for x in ["function", "parameter"]]):
            type_categories["function_parameters"].append(fact)

        # local variables
        elif "variable" in fact:
            type_categories["local_variables"].append(fact)
        else:
            others.append(fact)

    if others:
        print(others)
        raise Exception("Some unknown entry syntax in facts")

    return type_categories


def format_type(_types, is_ml=False):
    # TODO: Improve code quality
    type_formatted = []
    if _types:
        for _type in _types:
            i_type_list = []
            if is_ml:
                if is_ml and _type.startswith("Union["):
                    # TODO: Improve code, should not lower() for all. e.g., MyClass
                    types_split = [
                        x.replace(" ", "").lower()
                        for x in _type.split("Union[")[1].split("]")[0].split(",")
                    ]
                    i_type_list.extend(types_split)
                else:
                    # TODO: Maybe no translation should be done here
                    i_type_list.append(_type.lower())
                    # i_type_list.append(_t.split("[")[0].lower())
            else:
                for _t in _type:
                    if _t and _t.startswith("Union["):
                        types_split = [
                            x.replace(" ", "").lower()
                            for x in _t.split("Union[")[1].split("]")[0].split(",")
                        ]
                        i_type_list.extend(types_split)
                    elif _t and _t.startswith("Optional["):
                        types_split = [
                            x.replace(" ", "").lower()
                            for x in _t.split("Optional[")[1].split("]")[0].split(",")
                        ]
                        types_split.append("Nonetype")
                        i_type_list.extend(types_split)
                    elif _t and _t.startswith("Type["):
                        types_split = [
                            x.replace(" ", "").lower()
                            for x in _t.split("Type[")[1].split("]")[0].split(",")
                        ]
                        i_type_list.extend(types_split)
                    elif _t and _t in ["None", "Unknown"]:
                        i_type_list.append("Nonetype")
                    else:
                        # TODO: Maybe no translation should be done here
                        if _t:
                            i_type_list.append(_t.lower())
                        # i_type_list.append(_t.split("[")[0].lower())
            type_formatted.append(list(set(i_type_list)))

    for i in range(len(type_formatted)):
        for j in range(len(type_formatted[i])):
            type_formatted[i][j] = transform_type_string(type_formatted[i][j])
    return type_formatted


def transform_type_string(s: str) -> str:
    if "[" in s:
        # Use regular expression to replace content inside square brackets with empty string
        s = re.sub(r"\[.*\]", "", s)
        if s != "":
            # Convert the first letter to lower-case
            s = s[0].lower() + s[1:]
    if s == "None":
        s = "Nonetype"
    return s


def check_match(
    expected,
    out,
    partial_match=False,
    top_n=1,
    is_ml=False,
    print_mismatch=False,
    metadata={},
):
    if not all(
        [
            x in expected
            for x in out.keys()
            if x not in ["type", "all_type_preds", "col_offset"]
        ]
    ):
        return False

    # check if file match
    if expected.get("file") != out.get("file"):
        return False

    # # check if line_number match
    # if expected.get("line_number") != out.get("line_number"):
    #     return False

    # # if "col_offset" in expected and "col_offset" in out:
    # if expected["col_offset"] != out["col_offset"]:
    #     return False

    # check if function match
    if "function" in expected:
        if expected.get("function") != out.get("function"):
            return False

    # Check if parameters match
    if "parameter" in expected:
        if expected.get("parameter") != out.get("parameter"):
            return False

    # Check if variable match
    if "variable" in expected:
        if expected.get("variable") != out.get("variable"):
            return False

    # logger.debug("Other facts match: checking for types")
    type_formatted = []
    # check if type match
    if is_ml:
        # _type = out.get("type")
        _types = []
        if out.get("all_type_preds"):
            _types = [x[0] for x in out.get("all_type_preds")]
            type_formatted = format_type(_types, True)
    else:
        _types = [list(set(out.get("type")))]
        type_formatted = format_type(_types)

    expected_type_formatted = format_type([list(set(expected.get("type")))])
    # print(type_formatted)
    if partial_match:
        # check if atleast one exists
        matched = False
        for _t_list in type_formatted[:top_n]:
            for _t in _t_list:
                if any(_t in t for t in expected_type_formatted):
                    matched = True
    else:
        matched = False
        # if sorted(expected_type_formatted) == type_formatted[:top_n]:
        for _t_list in type_formatted[:top_n]:
            if sorted(expected_type_formatted) == [_t_list]:
                matched = True

    if not matched:
        # print only full mismatch
        if print_mismatch:
            logger.debug(
                f"\n\n##### Type mismatch! #####\nPartial mactching: {partial_match}"
            )

            with open(f"{metadata['tool_name']}_mismatches_reasons.csv", "a") as f:
                f.write(
                    ";".join(
                        [
                            metadata["cat"],
                            metadata["type_category"],
                            json.dumps(expected),
                            json.dumps(out),
                        ]
                    )
                )
                f.write("\n")

            logger.debug("Ground Truth:")
            logger.debug(json.dumps(expected, indent=4))

            logger.debug("Output:")
            logger.debug(json.dumps(out, indent=4))

            logger.debug("####################\n\n")

        return False

    return True


def measure_precision(out, expected, tool_name=None, print_mismatch=False):
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sort_facts(data_out)
    data_expected = sort_facts(data_expected)

    data_out_categories = categorize_facts(data_out)
    data_expected_categories = categorize_facts(data_expected)

    results = {
        "num_all": len(data_out),
        "num_caught_exact": 0,
        "num_caught_partial": 0,
    }

    results_only_cat = {
        k: {
            "num_all": len(data_out_categories[k]),
            "num_caught_exact": 0,
            "num_caught_partial": 0,
        }
        for k in TYPE_CATEGORIES
    }

    results_cat = {
        k_n: {
            k: {
                "num_all": len(data_out_categories[k]),
                "num_caught_exact": 0,
                "num_caught_partial": 0,
            }
            for k in TYPE_CATEGORIES
        }
        for k_n in TOP_N
    }

    if results["num_all"] != sum(
        [x["num_all"] for x in results_cat[TOP_N[0]].values()]
    ):
        raise Exception("results['num_all'] != results_cat['num_all']")

    if tool_name in ML_TOOLS:
        # For ML tools, top-n needs to be calculated separately
        for _n in TOP_N:
            for _cat, _cat_facts in data_out_categories.items():
                for fact_out in _cat_facts:
                    found_exact = False
                    found_partial = False
                    for fact_expected in data_expected:
                        # Check exact matches
                        if (
                            check_match(
                                expected=fact_expected,
                                out=fact_out,
                                top_n=_n,
                                is_ml=True,
                                print_mismatch=(
                                    True if (_n == 1 and print_mismatch) else False
                                ),
                                metadata={
                                    "tool_name": tool_name,
                                    "type_category": _cat,
                                    "cat": " -> ".join(expected.split("/")[-4:]),
                                },
                            )
                            and not found_exact
                        ):
                            if _n == 1:
                                # Only if top-1 for "results" list
                                results["num_caught_exact"] += 1
                            results_cat[_n][_cat]["num_caught_exact"] += 1
                            found_exact = True

                        # Check partial matches
                        elif (
                            check_match(
                                expected=fact_expected,
                                out=fact_out,
                                partial_match=True,
                                top_n=_n,
                                is_ml=True,
                            )
                            and not found_exact
                            and not found_partial
                        ):
                            for _type in fact_expected.get("type", []):
                                if _type in fact_out.get("type", []):
                                    if _n == 1:
                                        # Only if top-1 for "results" list
                                        results["num_caught_partial"] += 1
                                    results_cat[_n][_cat]["num_caught_partial"] += 1
                                    found_partial = True

    else:
        for _cat, _cat_facts in data_out_categories.items():
            for fact_out in _cat_facts:
                found_exact = False
                found_partial = False
                for fact_expected in data_expected:
                    # Check exact matches
                    if (
                        check_match(
                            expected=fact_expected,
                            out=fact_out,
                            print_mismatch=print_mismatch,
                            metadata={
                                "tool_name": tool_name,
                                "type_category": _cat,
                                "cat": " -> ".join(expected.split("/")[-4:]),
                            },
                        )
                        and not found_exact
                    ):
                        results["num_caught_exact"] += 1
                        results_only_cat[_cat]["num_caught_exact"] += 1
                        found_exact = True
                    # Check partial matches
                    elif (
                        check_match(
                            expected=fact_expected,
                            out=fact_out,
                            partial_match=True,
                        )
                        and not found_partial
                        and not found_exact
                    ):
                        results["num_caught_partial"] += 1
                        results_only_cat[_cat]["num_caught_partial"] += 1
                        found_partial = True

    return results, results_cat, results_only_cat


def measure_recall(out, expected, tool_name=None, print_missed=False):
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sort_facts(data_out)
    data_expected = sort_facts(data_expected)

    data_out_categories = categorize_facts(data_out)
    data_expected_categories = categorize_facts(data_expected)

    results = {
        "num_all": len(data_expected),
        "num_caught_exact": 0,
        "num_caught_partial": 0,
    }

    results_only_cat = {
        k: {
            "num_all": len(data_out_categories[k]),
            "num_caught_exact": 0,
            "num_caught_partial": 0,
        }
        for k in TYPE_CATEGORIES
    }

    results_cat = {
        k_n: {
            k: {
                "num_all": len(data_expected_categories[k]),
                "num_caught_exact": 0,
                "num_caught_partial": 0,
            }
            for k in TYPE_CATEGORIES
        }
        for k_n in TOP_N
    }

    if results["num_all"] != sum(
        [x["num_all"] for x in results_cat[TOP_N[0]].values()]
    ):
        raise Exception("results['num_all'] != results_cat['num_all']")

    if tool_name in ML_TOOLS:
        # For ML tools, top-n needs to be calculated separately
        for _n in TOP_N:
            for _cat, _cat_facts in data_expected_categories.items():
                for fact_expected in _cat_facts:
                    found_exact = False
                    found_partial = False
                    expected_found = False
                    for fact_out in data_out:
                        # Check exact matches
                        if (
                            check_match(
                                expected=fact_expected,
                                out=fact_out,
                                top_n=_n,
                                is_ml=True,
                            )
                            and not found_exact
                        ):
                            if _n == 1:
                                # Only if top-1 for "results" list
                                results["num_caught_exact"] += 1
                                expected_found = True
                            found_exact = True
                            results_cat[_n][_cat]["num_caught_exact"] += 1

                        # Check partial matches
                        elif (
                            check_match(
                                expected=fact_expected,
                                out=fact_out,
                                partial_match=True,
                                top_n=_n,
                                is_ml=True,
                            )
                            and not found_partial
                            and not found_exact
                        ):
                            if _n == 1:
                                # Only if top-1 for "results" list
                                results["num_caught_partial"] += 1
                            results_cat[_n][_cat]["num_caught_partial"] += 1
                            found_partial = True

                    if not expected_found and print_missed:
                        with open(f"{tool_name}_not_found_reasons.csv", "a") as f:
                            f.write(
                                ";".join(
                                    [
                                        " -> ".join(expected.split("/")[-4:]),
                                        _cat,
                                        json.dumps(fact_expected),
                                    ]
                                )
                            )
                            f.write("\n")

    else:
        for _cat, _cat_facts in data_expected_categories.items():
            for fact_expected in _cat_facts:
                expected_found = False
                found_exact = False
                found_partial = False
                for fact_out in data_out:
                    # Check exact matches
                    if (
                        check_match(expected=fact_expected, out=fact_out)
                        and not found_exact
                    ):
                        results["num_caught_exact"] += 1
                        results_only_cat[_cat]["num_caught_exact"] += 1
                        expected_found = True
                        found_exact = True
                    # Check partial matches
                    elif (
                        check_match(
                            expected=fact_expected, out=fact_out, partial_match=True
                        )
                        and not found_exact
                        and not found_partial
                    ):
                        results["num_caught_partial"] += 1
                        results_only_cat[_cat]["num_caught_partial"] += 1
                        found_partial = True

                if not expected_found and print_missed:
                    logger.debug(f"~~~~~~ Type Not Found! ~~~~~~")

                    with open(f"{tool_name}_not_found_reasons.csv", "a") as f:
                        f.write(
                            ";".join(
                                [
                                    " -> ".join(expected.split("/")[-4:]),
                                    _cat,
                                    json.dumps(fact_expected),
                                ]
                            )
                        )
                        f.write("\n")

                    logger.debug("Expected:")
                    logger.debug(json.dumps(fact_expected, indent=4))

                    logger.debug("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    return results, results_cat, results_only_cat


def equal_sound(out, expected):
    """
    No False Negatives in the output.
    i.e., all facts in the ground truth should be contained in the output
    """
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sort_facts(data_out)
    data_expected = sort_facts(data_expected)

    for fact_expected in data_expected:
        fact_expected_exists = False
        for fact_out in data_out:
            if check_match(expected=fact_expected, out=fact_out):
                fact_expected_exists = True
                break
        if not fact_expected_exists:
            # A false negative is found
            return 0

    # No false negatives
    return 1


def equal_complete(out, expected):
    """
    No False Positives in the output.
    i.e., all facts in the output should be contained in the ground truth
    """
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sort_facts(data_out)
    data_expected = sort_facts(data_expected)

    for fact_out in data_out:
        fact_out_exists = False
        for fact_expected in data_expected:
            if check_match(expected=fact_expected, out=fact_out):
                fact_out_exists = True
                break

        if not fact_out_exists:
            # A false positive is found
            return 0

    # No false positives
    return 1


def get_fact_stats(json_files):
    total_annotations = 0
    rows = []
    sum_functions = 0
    sum_params = 0
    sum_variables = 0
    for json_file in json_files:
        with open(json_file, "r") as f:
            data = json.load(f)
            total_annotations += len(data)
            merged_cell = json_file
            for _t in data:
                line_number = _t.get("line_number", "")
                function = _t.get("function", "")
                param = _t.get("parameter", "")
                variable = _t.get("variable", "")
                types = ", ".join(_t.get("type", []))
                rows.append(
                    [
                        merged_cell,
                        line_number,
                        function,
                        param,
                        variable,
                        types,
                    ]
                )
                if function:
                    if not param and not variable:
                        sum_functions += 1

                if param:
                    sum_params += 1

                if variable:
                    sum_variables += 1

    return (
        total_annotations,
        sum_functions,
        sum_params,
        sum_variables,
    )


def benchmark_count(benchmark_path):
    total_result = []
    for cat in sorted(os.listdir(benchmark_path)):
        cat_dir = os.path.join(benchmark_path, cat)
        json_files = [_file for _file in sorted(Path(cat_dir).rglob("*_gt.json"))]

        _a, _functions, _params, _variables = get_fact_stats(json_files)
        total_result.append([cat, _a, _functions, _params, _variables])
    return total_result


def normalize_type(type_str, nested_level=0):
    """
    Normalize the type string by removing module prefixes and simplifying typing constructs.
    Example: 'builtins.str' -> 'str',
             'typing.Tuple[builtins.str, builtins.float]' -> 'Tuple[str, float]',
             'musictaxonomy.spotify.models.spotifyuser' -> 'SpotifyUser',
             'List[List[Tuple[str]]]' -> 'List[List[Any]]' if nested level > 2.
    """

    if type_str is None:
        return None

    # Remove extra quotes if present
    if type_str.startswith('"') and type_str.endswith('"'):
        type_str = type_str.strip('"')

    # Mapping of module prefixes to remove
    type_mappings = {
        "builtins.": "",
        "typing.": "",
    }
    # Additional type mappings
    additional_type_mappings = {
        "integer": "int",
        "string": "str",
        "dictonary": "dict",
        "method": "Callable",
        "func": "Callable",
        "function": "Callable",
        "none": "None",
        "Nonetype": "None",
        "nonetype": "None",
        "NoneType": "None",
        "Text": "str",
    }

    if type_str is None:
        return None

    # Replace module prefixes
    for prefix, replacement in type_mappings.items():
        type_str = type_str.replace(prefix, replacement)

    # Apply additional type mappings
    type_str = additional_type_mappings.get(type_str, type_str)

    # Handle generic types (e.g., Tuple[], List[], Dict[])
    if "[" in type_str and "]" in type_str:
        base_type, generic_content = type_str.split("[", 1)
        generic_content = generic_content.rsplit("]", 1)[0]
        # Process the generic parameters recursively
        generic_params = []
        bracket_level = 0
        param = ""
        for char in generic_content:
            if char == "[":
                bracket_level += 1
                param += char
            elif char == "]":
                bracket_level -= 1
                param += char
            elif char == "," and bracket_level == 0:
                generic_params.append(param.strip())
                param = ""
            else:
                param += char
        if param:
            generic_params.append(param.strip())

        # If nested level is greater than 0, replace with Any
        if nested_level > 0:
            normalized_params = ["Any"]
        else:
            normalized_params = [
                normalize_type(param, nested_level + 1) for param in generic_params
            ]

        return f"{base_type}[{', '.join(normalized_params)}]"

    # Handle fully qualified names by extracting the last segment
    if "." in type_str:
        return type_str.split(".")[-1]

    # Return the simplified type
    return type_str


def normalize_types(types):
    """
    Normalize the type strings in the data.
    """
    return [normalize_type(type_str) for type_str in types]
