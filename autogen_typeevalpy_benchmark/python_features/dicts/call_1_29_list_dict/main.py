# A dictionary containing functions as values is created.


def func1():
    return [70, 22, 57]


def func2():
    return {'kajwm': 87, 'cbvfl': 15, 'yyqqj': 56}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
