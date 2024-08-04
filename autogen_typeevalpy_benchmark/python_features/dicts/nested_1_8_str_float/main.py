# Use a nested dictionary and assign a value to it.


def func1():
    return 'hbicp'


def func2():
    return 61.48


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
