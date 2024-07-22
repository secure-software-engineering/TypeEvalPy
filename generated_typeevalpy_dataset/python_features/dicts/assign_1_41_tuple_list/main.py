# A dictionary key is assigned to a function.


def func1():
    return (14, 63, 39)


def func2():
    return [92, 39, 76]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
