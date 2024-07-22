# Use a nested dictionary and assign a value to it.


def func1():
    return 77.66


def func2():
    return 'pyyqp'


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
