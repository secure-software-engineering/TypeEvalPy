# Use a nested dictionary and assign a value to it.


def func1():
    return 95


def func2():
    return 85.04


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
