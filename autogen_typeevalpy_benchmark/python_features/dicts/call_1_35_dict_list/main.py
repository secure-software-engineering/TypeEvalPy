# A dictionary containing functions as values is created.


def func1():
    return {'uniek': 47, 'msawn': 61, 'pffdo': 65}


def func2():
    return [95, 14, 52]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
