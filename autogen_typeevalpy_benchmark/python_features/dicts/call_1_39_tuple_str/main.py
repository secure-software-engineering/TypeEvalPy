# A dictionary containing functions as values is created.


def func1():
    return (56, 26, 11)


def func2():
    return 'gfccl'


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
