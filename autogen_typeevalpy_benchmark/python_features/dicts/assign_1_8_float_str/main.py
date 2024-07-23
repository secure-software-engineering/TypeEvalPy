# A dictionary key is assigned to a function.


def func1():
    return 67.15


def func2():
    return 'xlhqg'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
