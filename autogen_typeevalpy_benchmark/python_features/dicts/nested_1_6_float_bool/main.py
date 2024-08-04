# Use a nested dictionary and assign a value to it.


def func1():
    return 15.91


def func2():
    return False


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
