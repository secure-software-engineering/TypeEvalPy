# Use a nested dictionary and assign a value to it.


def func1():
    return <value1>


def func2():
    return <value2>


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
