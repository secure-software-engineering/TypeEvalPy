# A dictionary containing functions as values is created.


def func1():
    return 81


def func2():
    return {'cypoy': 15, 'gbngl': 63, 'hbvkl': 8}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
