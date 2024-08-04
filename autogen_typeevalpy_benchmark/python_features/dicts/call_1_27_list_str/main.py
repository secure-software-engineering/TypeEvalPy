# A dictionary containing functions as values is created.


def func1():
    return [63, 38, 98]


def func2():
    return 'hyhwp'


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
