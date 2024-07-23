# A dictionary containing functions as values is created.


def func1():
    return [51, 95, 81]


def func2():
    return 55


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
