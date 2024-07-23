# A dictionary key is assigned to a function.


def func1():
    return 51


def func2():
    return [75, 39, 37]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
