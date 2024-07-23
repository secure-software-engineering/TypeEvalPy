# A dictionary containing functions as values is created.


def func1():
    return 37.96


def func2():
    return {'yilzz': 22, 'gnnzm': 24, 'zlljz': 45}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
