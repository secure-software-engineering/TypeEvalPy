# A dictionary containing functions as values is created.


def func1():
    return (67, 96, 1)


def func2():
    return [40, 44, 1]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
