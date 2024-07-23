# A dictionary key is assigned to a function.


def func1():
    return [77, 36, 96]


def func2():
    return 52


d = {"a": func1}

d["a"] = func2

e = d["a"]()
