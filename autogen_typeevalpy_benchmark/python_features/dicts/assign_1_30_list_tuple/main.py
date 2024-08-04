# A dictionary key is assigned to a function.


def func1():
    return [27, 47, 4]


def func2():
    return (15, 52, 91)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
