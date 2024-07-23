# A dictionary key is assigned to a function.


def func1():
    return 'ztjly'


def func2():
    return 62


d = {"a": func1}

d["a"] = func2

e = d["a"]()
