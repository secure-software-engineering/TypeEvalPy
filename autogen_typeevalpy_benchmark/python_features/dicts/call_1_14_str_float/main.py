# A dictionary containing functions as values is created.


def func1():
    return 'lcvuy'


def func2():
    return 29.2


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
