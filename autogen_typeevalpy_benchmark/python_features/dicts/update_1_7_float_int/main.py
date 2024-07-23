# The update method of dictionaries is used.


def func1():
    return 61


def func2():
    return 25.4


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
