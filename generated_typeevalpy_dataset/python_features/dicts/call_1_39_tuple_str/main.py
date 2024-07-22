# A dictionary containing functions as values is created.


def func1():
    return (74, 23, 4)


def func2():
    return 'jshpq'


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
