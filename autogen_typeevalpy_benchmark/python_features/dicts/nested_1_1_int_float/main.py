# Use a nested dictionary and assign a value to it.


def func1():
    return 16


def func2():
    return 54.38


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
