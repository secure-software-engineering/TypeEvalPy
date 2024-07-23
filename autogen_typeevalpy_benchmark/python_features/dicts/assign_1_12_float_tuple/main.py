# A dictionary key is assigned to a function.


def func1():
    return 20.16


def func2():
    return (31, 74, 3)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
