# A dictionary containing functions as values is created.


def func1():
    return {'vibyd': 20, 'thdam': 20, 'jrtve': 80}


def func2():
    return (90, 40, 13)


d = {"a": func1, 1: func2, 2: 3}

e = d["a"]()
f = d[1]()
