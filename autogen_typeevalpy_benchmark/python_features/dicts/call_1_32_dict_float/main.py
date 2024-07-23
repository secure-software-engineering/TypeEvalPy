# A dictionary containing functions as values is created.


def func1():
    return {'aywav': 23, 'qnhnp': 21, 'kjpag': 64}


def func2():
    return 64.14


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
