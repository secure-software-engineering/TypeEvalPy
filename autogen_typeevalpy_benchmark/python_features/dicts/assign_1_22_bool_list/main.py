# A dictionary key is assigned to a function.


def func1():
    return True


def func2():
    return [34, 15, 49]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
