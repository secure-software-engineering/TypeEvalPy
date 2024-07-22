# A dictionary containing functions as values is created.


def func1():
    return [46, 77, 36]


def func2():
    return True


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
