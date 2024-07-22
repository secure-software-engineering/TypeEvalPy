# A dictionary key is assigned to a function.


def func1():
    return [90, 60, 10]


def func2():
    return 14


d = {"a": func1}

d["a"] = func2

e = d["a"]()
