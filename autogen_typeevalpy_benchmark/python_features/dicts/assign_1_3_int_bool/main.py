# A dictionary key is assigned to a function.


def func1():
    return 49


def func2():
    return True


d = {"a": func1}

d["a"] = func2

e = d["a"]()
