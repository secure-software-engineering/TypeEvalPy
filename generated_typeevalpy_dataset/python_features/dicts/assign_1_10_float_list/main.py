# A dictionary key is assigned to a function.


def func1():
    return 89.8


def func2():
    return [50, 32, 33]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
