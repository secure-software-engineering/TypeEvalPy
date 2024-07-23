# Use a nested dictionary and assign a value to it.


def func1():
    return 12


def func2():
    return 'mvihl'


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
