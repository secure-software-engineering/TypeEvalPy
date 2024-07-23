# A dictionary containing functions as values is created.


def func1():
    return (94, 27, 75)


def func2():
    return 21


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
