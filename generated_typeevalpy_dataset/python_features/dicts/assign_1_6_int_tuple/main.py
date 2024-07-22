# A dictionary key is assigned to a function.


def func1():
    return 24


def func2():
    return (29, 19, 64)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
