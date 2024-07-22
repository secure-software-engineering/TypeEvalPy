# A dictionary containing functions as values is created.


def func1():
    return 48.38


def func2():
    return {'bwmlq': 29, 'vkegs': 52, 'pdyyo': 39}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
