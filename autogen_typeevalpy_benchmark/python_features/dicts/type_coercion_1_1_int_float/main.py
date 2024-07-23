# Check if tool type coerces integer and string values.


def func1():
    return 87


def func2():
    return 49.7


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
