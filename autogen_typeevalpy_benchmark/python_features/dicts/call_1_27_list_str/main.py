# A dictionary containing functions as values is created.


def func1():
    return [11, 98, 60]


def func2():
    return 'yuwet'


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
