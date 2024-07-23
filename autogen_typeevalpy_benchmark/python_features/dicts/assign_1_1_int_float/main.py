# A dictionary key is assigned to a function.


def func1():
    return 1


def func2():
    return 99.27


d = {"a": func1}

d["a"] = func2

e = d["a"]()
