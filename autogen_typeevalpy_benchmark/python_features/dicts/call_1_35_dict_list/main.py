# A dictionary containing functions as values is created.


def func1():
    return {'mkinz': 90, 'gepzn': 91, 'srjjm': 92}


def func2():
    return [66, 86, 15]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
