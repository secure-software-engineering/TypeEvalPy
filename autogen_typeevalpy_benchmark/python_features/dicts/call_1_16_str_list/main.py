# A dictionary containing functions as values is created.


def func1():
    return 'jibgj'


def func2():
    return [96, 88, 10]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
