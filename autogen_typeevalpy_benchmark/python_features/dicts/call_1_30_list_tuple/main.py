# A dictionary containing functions as values is created.


def func1():
    return [42, 49, 68]


def func2():
    return (5, 51, 94)


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
