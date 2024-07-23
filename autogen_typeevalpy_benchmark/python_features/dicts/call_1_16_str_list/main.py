# A dictionary containing functions as values is created.


def func1():
    return 'ukxpl'


def func2():
    return [14, 17, 95]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
