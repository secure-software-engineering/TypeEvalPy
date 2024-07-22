# A dictionary containing functions as values is created.


def func1():
    return 66.95


def func2():
    return (49, 53, 45)


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
