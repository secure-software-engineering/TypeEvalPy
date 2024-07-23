# Use a nested dictionary and assign a value to it.


def func1():
    return 'vyoaa'


def func2():
    return 96.31


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
