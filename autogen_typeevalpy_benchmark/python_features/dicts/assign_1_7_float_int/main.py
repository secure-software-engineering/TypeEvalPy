# A dictionary key is assigned to a function.


def func1():
    return 30.71


def func2():
    return 18


d = {"a": func1}

d["a"] = func2

e = d["a"]()
