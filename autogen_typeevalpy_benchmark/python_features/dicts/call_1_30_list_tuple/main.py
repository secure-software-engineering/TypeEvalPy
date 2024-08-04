# A dictionary containing functions as values is created.


def func1():
    return [22, 34, 30]


def func2():
    return (63, 97, 6)


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
