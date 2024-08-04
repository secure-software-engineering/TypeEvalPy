# A dictionary containing functions as values is created.


def func1():
    return {'dpnks': 24, 'cqlyv': 31, 'qpmar': 55}


def func2():
    return 75.19


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
