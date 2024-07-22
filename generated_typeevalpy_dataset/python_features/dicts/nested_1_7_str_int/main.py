# Use a nested dictionary and assign a value to it.


def func1():
    return 'kzuza'


def func2():
    return 25


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
