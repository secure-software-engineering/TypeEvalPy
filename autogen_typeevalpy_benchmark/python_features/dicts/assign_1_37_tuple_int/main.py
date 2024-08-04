# A dictionary key is assigned to a function.


def func1():
    return (96, 82, 72)


def func2():
    return 98


d = {"a": func1}

d["a"] = func2

e = d["a"]()
