# A dictionary key is assigned to a function.


def func1():
    return (76, 35, 57)


def func2():
    return 42


d = {"a": func1}

d["a"] = func2

e = d["a"]()
