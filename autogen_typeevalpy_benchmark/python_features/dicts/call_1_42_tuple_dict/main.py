# A dictionary containing functions as values is created.


def func1():
    return (50, 44, 61)


def func2():
    return {'wbygt': 14, 'ekcmt': 40, 'ovlta': 77}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
