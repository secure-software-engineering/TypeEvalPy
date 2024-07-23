# A dictionary key is assigned to a function.


def func1():
    return 'ckbbu'


def func2():
    return 11.22


d = {"a": func1}

d["a"] = func2

e = d["a"]()
