# A dictionary containing functions as values is created.


def func1():
    return (78, 27, 18)


def func2():
    return {'exort': 41, 'xgejo': 89, 'elhtj': 51}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
