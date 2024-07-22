# A dictionary key is assigned to a function.


def func1():
    return 'xtcoc'


def func2():
    return [16, 93, 67]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
