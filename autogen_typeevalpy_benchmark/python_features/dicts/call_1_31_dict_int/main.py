# A dictionary containing functions as values is created.


def func1():
    return {'vnvem': 99, 'ikbdi': 63, 'oygkz': 84}


def func2():
    return 6


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
