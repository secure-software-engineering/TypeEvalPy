# A dictionary key is assigned to a function.


def func1():
    return (97, 93, 7)


def func2():
    return 72.39


d = {"a": func1}

d["a"] = func2

e = d["a"]()
