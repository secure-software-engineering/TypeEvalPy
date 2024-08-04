# A dictionary containing functions as values is created.


def func1():
    return [59, 5, 78]


def func2():
    return 36.05


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
