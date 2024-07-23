# A dictionary containing functions as values is created.


def func1():
    return (59, 71, 10)


def func2():
    return 16.89


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
