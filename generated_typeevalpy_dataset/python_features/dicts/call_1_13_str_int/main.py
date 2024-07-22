# A dictionary containing functions as values is created.


def func1():
    return 'mnvyu'


def func2():
    return 66


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
