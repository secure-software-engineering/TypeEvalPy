# A dictionary containing functions as values is created.


def func1():
    return {'rzcsl': 35, 'qzqyu': 59, 'twcav': 59}


def func2():
    return [49, 66, 32]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
