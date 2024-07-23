# A dictionary key is assigned to a function.


def func1():
    return 88.68


def func2():
    return [50, 67, 97]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
