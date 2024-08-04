# A dictionary key is assigned to a function.


def func1():
    return 'wufys'


def func2():
    return 8.52


d = {"a": func1}

d["a"] = func2

e = d["a"]()
