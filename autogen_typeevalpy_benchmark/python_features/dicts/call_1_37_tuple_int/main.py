# A dictionary containing functions as values is created.


def func1():
    return (27, 34, 89)


def func2():
    return 49


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
