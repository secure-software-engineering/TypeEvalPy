import csv
import json

ML_TOOLS = ["type4py"]
STANDARD_TOOLS = ["scalpel"]
TOP_N = [1, 3, 5]

TYPE_CATEGORIES = ["function_returns", "function_parameters", "local_variables"]


def sort_facts(data):
    data = sorted(data, key=lambda x: x["line_number"])
    for fact in data:
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


def check_match(expected, out, partial_match=False, top_n=1, is_ml=False):
    if not all(
        [x in expected for x in out.keys() if x not in ["type", "all_type_preds"]]
    ):
        return False

    # check if file match
    if expected.get("file") != out.get("file"):
        return False

    # check if line_number match
    if expected.get("line_number") != out.get("line_number"):
        return False

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

    # check if type match
    if is_ml:
        # _type = out.get("type")
        _type = []
        if out.get("all_type_preds"):
            _type = [x[0] for x in out.get("all_type_preds")]
    else:
        _type = out.get("type")

    type_formatted = []
    if _type:
        for _t in _type:
            if _t.startswith("Union["):
                types_split = [
                    x.replace(" ", "").lower()
                    for x in _t.split("Union[")[1].split("]")[0].split(",")
                ]
                type_formatted.append(types_split)
            else:
                type_formatted.append([_t.split("[")[0].lower()])

    if partial_match:
        # check if atleast one exists
        matched = False
        for _t_list in type_formatted[:top_n]:
            for _t in _t_list:
                if _t in expected["type"]:
                    matched = True

        if not matched:
            return False
    else:
        matched = False
        for _t_list in type_formatted[:top_n]:
            if sorted(expected.get("type")) == sorted(_t_list):
                matched = True

        if not matched:
            return False

    return True


def measure_precision(out, expected, tool_name=None):
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
                    for fact_expected in data_expected:
                        # Check exact matches
                        if check_match(
                            expected=fact_expected, out=fact_out, top_n=_n, is_ml=True
                        ):
                            if _n == 1:
                                # Only if top-1 for "results" list
                                results["num_caught_exact"] += 1
                            results_cat[_n][_cat]["num_caught_exact"] += 1
                        # Check partial matches
                        elif check_match(
                            expected=fact_expected,
                            out=fact_out,
                            partial_match=True,
                            top_n=_n,
                            is_ml=True,
                        ):
                            for _type in fact_expected.get("type", []):
                                if _type in fact_out.get("type", []):
                                    if _n == 1:
                                        # Only if top-1 for "results" list
                                        results["num_caught_partial"] += 1
                                    results_cat[_n][_cat]["num_caught_partial"] += 1

    else:
        for _cat, _cat_facts in data_out_categories.items():
            for fact_out in _cat_facts:
                for fact_expected in data_expected:
                    # Check exact matches
                    if check_match(expected=fact_expected, out=fact_out):
                        results["num_caught_exact"] += 1
                        results_only_cat[_cat]["num_caught_exact"] += 1
                    # Check partial matches
                    elif check_match(
                        expected=fact_expected, out=fact_out, partial_match=True
                    ):
                        results["num_caught_partial"] += 1
                        results_only_cat[_cat]["num_caught_partial"] += 1

    return results, results_cat, results_only_cat


def measure_recall(out, expected, tool_name=None):
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
                    for fact_out in data_out:
                        # Check exact matches
                        if check_match(
                            expected=fact_expected, out=fact_out, top_n=_n, is_ml=True
                        ):
                            if _n == 1:
                                # Only if top-1 for "results" list
                                results["num_caught_exact"] += 1
                            results_cat[_n][_cat]["num_caught_exact"] += 1

                        # Check partial matches
                        elif check_match(
                            expected=fact_expected,
                            out=fact_out,
                            partial_match=True,
                            top_n=_n,
                            is_ml=True,
                        ):
                            if _n == 1:
                                # Only if top-1 for "results" list
                                results["num_caught_partial"] += 1
                            results_cat[_n][_cat]["num_caught_partial"] += 1

    else:
        for _cat, _cat_facts in data_expected_categories.items():
            for fact_expected in _cat_facts:
                for fact_out in data_out:
                    # Check exact matches
                    if check_match(expected=fact_expected, out=fact_out):
                        results["num_caught_exact"] += 1
                        results_only_cat[_cat]["num_caught_exact"] += 1

                    # Check partial matches
                    elif check_match(
                        expected=fact_expected, out=fact_out, partial_match=True
                    ):
                        results["num_caught_partial"] += 1
                        results_only_cat[_cat]["num_caught_partial"] += 1

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
            if fact_out == fact_expected:
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
            if fact_out == fact_expected:
                fact_out_exists = True
                break

        if not fact_out_exists:
            # A false positive is found
            return 0

    # No false positives
    return 1
