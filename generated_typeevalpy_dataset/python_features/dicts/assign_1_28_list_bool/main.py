# A dictionary key is assigned to a function.


def func1():
    return [82, 32, 85]


def func2():
    return False


d = {"a": func1}

d["a"] = func2

e = d["a"]()
