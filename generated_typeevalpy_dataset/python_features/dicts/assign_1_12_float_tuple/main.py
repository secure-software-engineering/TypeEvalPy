# A dictionary key is assigned to a function.


def func1():
    return 95.64


def func2():
    return (7, 47, 50)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
