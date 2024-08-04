# A dictionary key is assigned to a function.


def func1():
    return (44, 30, 37)


def func2():
    return False


d = {"a": func1}

d["a"] = func2

e = d["a"]()
