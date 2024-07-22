# A dictionary containing functions as values is created.


def func1():
    return 'nyqiq'


def func2():
    return 92.68


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
