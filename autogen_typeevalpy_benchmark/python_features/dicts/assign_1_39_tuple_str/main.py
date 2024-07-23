# A dictionary key is assigned to a function.


def func1():
    return (67, 80, 57)


def func2():
    return 'ffyxt'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
