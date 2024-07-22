# A dictionary key is assigned to a function.


def func1():
    return [6, 79, 14]


def func2():
    return 'hjbvv'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
