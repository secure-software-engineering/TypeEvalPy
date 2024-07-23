# Use a nested dictionary and assign a value to it.


def func1():
    return 63.5


def func2():
    return 65


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
