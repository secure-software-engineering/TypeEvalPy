# Use a nested dictionary and assign a value to it.


def func1():
    return 79.21


def func2():
    return 34


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
