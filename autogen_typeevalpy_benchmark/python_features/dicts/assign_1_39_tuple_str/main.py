# A dictionary key is assigned to a function.


def func1():
    return (1, 33, 72)


def func2():
    return 'zcafu'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
