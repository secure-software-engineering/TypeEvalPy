# A dictionary containing functions as values is created.


def func1():
    return 10.86


def func2():
    return [36, 89, 90]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
