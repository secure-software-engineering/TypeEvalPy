import json


def scalpel_translator(data):
    pass


def measure_precision(out, expected):
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sorted(data_out, key=lambda x: x["line_number"])
    data_expected = sorted(data_expected, key=lambda x: x["line_number"])

    results = {
        "num_all": len(data_out),
        "num_caught_exact": 0,
        "num_caught_partial": 0,
    }

    for fact_out in data_out:
        for fact_expected in data_expected:
            # Check exact matches
            if fact_out == fact_expected:
                results["num_caught_exact"] += 1
            # Check partial matches
            elif (fact_expected.keys() == fact_out.keys()) and all(
                [
                    fact_expected.get(x) == fact_out.get(x)
                    for x in fact_expected.keys()
                    if x != "type"
                ]
            ):
                for _type in fact_expected.get("type", []):
                    if _type in fact_out.get("type", []):
                        results["num_caught_partial"] += 1

    return results


def measure_recall(out, expected):
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sorted(data_out, key=lambda x: x["line_number"])
    data_expected = sorted(data_expected, key=lambda x: x["line_number"])

    results = {
        "num_all": len(data_expected),
        "num_caught_exact": 0,
        "num_caught_partial": 0,
    }

    for fact_expected in data_expected:
        for fact_out in data_out:
            if fact_out == fact_expected:
                results["num_caught_exact"] += 1
            elif (fact_expected.keys() == fact_out.keys()) and all(
                [
                    fact_expected.get(x) == fact_out.get(x)
                    for x in fact_expected.keys()
                    if x != "type"
                ]
            ):
                for _type in fact_expected.get("type", []):
                    if _type in fact_out.get("type", []):
                        results["num_caught_partial"] += 1

    return results


def equal_sound(out, expected):
    """
    No False Negatives in the output.
    i.e., all facts in the ground truth should be contained in the output
    """
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sorted(data_out, key=lambda x: x["line_number"])
    data_expected = sorted(data_expected, key=lambda x: x["line_number"])

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

    data_out = sorted(data_out, key=lambda x: x["line_number"])
    data_expected = sorted(data_expected, key=lambda x: x["line_number"])

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
