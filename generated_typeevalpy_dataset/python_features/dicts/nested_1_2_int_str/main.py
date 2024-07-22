# Use a nested dictionary and assign a value to it.


def func1():
    return 81


def func2():
    return 'oltlf'


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
