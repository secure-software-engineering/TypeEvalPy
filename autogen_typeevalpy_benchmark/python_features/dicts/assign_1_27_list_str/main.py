# A dictionary key is assigned to a function.


def func1():
    return [62, 65, 13]


def func2():
    return 'blpju'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
