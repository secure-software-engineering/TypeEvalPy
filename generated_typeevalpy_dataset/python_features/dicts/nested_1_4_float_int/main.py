# Use a nested dictionary and assign a value to it.


def func1():
    return 35.67


def func2():
    return 66


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
