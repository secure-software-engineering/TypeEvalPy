# A dictionary key is assigned to a function.


def func1():
    return [85, 58, 5]


def func2():
    return 18.49


d = {"a": func1}

d["a"] = func2

e = d["a"]()
