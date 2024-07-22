# A dictionary key is assigned to a function.


def func1():
    return 20.34


def func2():
    return 96


d = {"a": func1}

d["a"] = func2

e = d["a"]()
