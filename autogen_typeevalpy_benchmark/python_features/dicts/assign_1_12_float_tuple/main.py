# A dictionary key is assigned to a function.


def func1():
    return 14.3


def func2():
    return (15, 26, 23)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
