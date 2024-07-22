# A dictionary containing functions as values is created.


def func1():
    return True


def func2():
    return {'orlmy': 50, 'dnbbb': 52, 'wrknw': 16}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
