# A dictionary containing functions as values is created.


def func1():
    return (13, 82, 85)


def func2():
    return [60, 34, 39]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
