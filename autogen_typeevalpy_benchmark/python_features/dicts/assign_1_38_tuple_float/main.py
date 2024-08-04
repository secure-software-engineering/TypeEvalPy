# A dictionary key is assigned to a function.


def func1():
    return (82, 64, 22)


def func2():
    return 2.01


d = {"a": func1}

d["a"] = func2

e = d["a"]()
