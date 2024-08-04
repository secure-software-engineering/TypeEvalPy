# A dictionary containing functions as values is created.


def func1():
    return 92.68


def func2():
    return {'mgakz': 52, 'lauge': 80, 'ceftp': 81}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
