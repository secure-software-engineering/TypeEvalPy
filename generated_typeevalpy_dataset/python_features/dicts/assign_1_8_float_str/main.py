# A dictionary key is assigned to a function.


def func1():
    return 24.51


def func2():
    return 'fylxt'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
