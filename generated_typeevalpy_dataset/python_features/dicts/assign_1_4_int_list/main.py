# A dictionary key is assigned to a function.


def func1():
    return 70


def func2():
    return [13, 90, 2]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
