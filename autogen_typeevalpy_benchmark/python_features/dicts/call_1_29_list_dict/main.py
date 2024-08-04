# A dictionary containing functions as values is created.


def func1():
    return [56, 61, 27]


def func2():
    return {'ohdrq': 92, 'tjmpp': 61, 'mejtf': 28}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
