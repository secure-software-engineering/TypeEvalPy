# Use a nested dictionary and assign a value to it.


def func1():
    return 84.8


def func2():
    return True


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
