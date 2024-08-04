# A dictionary key is assigned to a function.


def func1():
    return [84, 3, 10]


def func2():
    return 28


d = {"a": func1}

d["a"] = func2

e = d["a"]()
