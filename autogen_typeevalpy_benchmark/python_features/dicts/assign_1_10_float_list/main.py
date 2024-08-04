# A dictionary key is assigned to a function.


def func1():
    return 76.49


def func2():
    return [68, 9, 12]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
