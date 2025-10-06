# A dictionary key is assigned to a function.


def func1():
    return "Hello from func1"


def func2():
    return 42


d = {"a": func1}

d["a"] = func2

e = d["a"]()
func1()
