# A dictionary key is assigned to a function.


def func1():
    return 'luszw'


def func2():
    return 28


d = {"a": func1}

d["a"] = func2

e = d["a"]()
