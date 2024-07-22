# A dictionary key is assigned to a function.


def func1():
    return [77, 9, 3]


def func2():
    return 24.88


d = {"a": func1}

d["a"] = func2

e = d["a"]()
