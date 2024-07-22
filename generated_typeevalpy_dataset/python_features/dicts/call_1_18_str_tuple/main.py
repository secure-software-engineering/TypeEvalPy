# A dictionary containing functions as values is created.


def func1():
    return 'efsnz'


def func2():
    return (76, 6, 67)


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
