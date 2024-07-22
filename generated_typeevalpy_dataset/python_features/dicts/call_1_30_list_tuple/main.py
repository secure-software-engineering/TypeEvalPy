# A dictionary containing functions as values is created.


def func1():
    return [3, 33, 9]


def func2():
    return (90, 76, 81)


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
