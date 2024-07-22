# A dictionary is passed as a parameter.


def func2():
    return 'fuftp'


def func1(d):
    return d["a"]()


d = {"a": func2}

e = func1(d)
