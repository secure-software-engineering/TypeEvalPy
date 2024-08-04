# A dictionary containing functions as values is created.


def func1():
    return False


def func2():
    return 73


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
