# The update method of dictionaries is used.


def func1():
    return 25


def func2():
    return 99.56


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
