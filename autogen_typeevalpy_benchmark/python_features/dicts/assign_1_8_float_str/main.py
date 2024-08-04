# A dictionary key is assigned to a function.


def func1():
    return 22.21


def func2():
    return 'enprv'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
