# A dictionary containing functions as values is created.


def func1():
    return {'ewqoz': 51, 'ikiuc': 67, 'ybgex': 84}


def func2():
    return 30


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
