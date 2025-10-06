# Use a nested dictionary and assign a value to it.


def func1():
    return 42


def func2():
    return "Hello from func2"


d = {"a": {"b": func1}}

d["a"]["b"] = func2

e = d["a"]["b"]()
func1()
