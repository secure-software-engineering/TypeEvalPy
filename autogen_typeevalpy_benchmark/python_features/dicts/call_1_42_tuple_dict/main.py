# A dictionary containing functions as values is created.


def func1():
    return (84, 30, 1)


def func2():
    return {'uqufo': 30, 'rkmge': 94, 'mozoc': 61}


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
