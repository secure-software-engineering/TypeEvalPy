# A dictionary key is assigned to a function.


def func1():
    return 75


def func2():
    return [67, 94, 49]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
