# Use a nested dictionary and assign a value to it.


def func1():
    return 74.29


def func2():
    return 'yjzto'


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
