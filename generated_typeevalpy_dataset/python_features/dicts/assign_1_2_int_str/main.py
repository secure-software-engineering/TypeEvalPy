# A dictionary key is assigned to a function.


def func1():
    return 26


def func2():
    return 'tfrtn'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
