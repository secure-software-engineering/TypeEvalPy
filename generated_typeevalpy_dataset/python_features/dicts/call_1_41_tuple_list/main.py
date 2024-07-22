# A dictionary containing functions as values is created.


def func1():
    return (3, 40, 63)


def func2():
    return [17, 100, 12]


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
