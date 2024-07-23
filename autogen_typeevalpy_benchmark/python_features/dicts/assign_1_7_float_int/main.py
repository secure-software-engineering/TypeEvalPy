# A dictionary key is assigned to a function.


def func1():
    return 90.15


def func2():
    return 17


d = {"a": func1}

d["a"] = func2

e = d["a"]()
