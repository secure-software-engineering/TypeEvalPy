# A dictionary is passed as a parameter.


def func2():
    return 99.25


def func1(d):
    return d["a"]()


d = {"a": func2}

e = func1(d)
