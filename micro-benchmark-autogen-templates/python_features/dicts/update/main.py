# The update method of dictionaries is used.


def func1():
    return 42


def func2():
    return "Hello from func2"


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
