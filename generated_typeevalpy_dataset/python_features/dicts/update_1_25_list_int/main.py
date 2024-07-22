# The update method of dictionaries is used.


def func1():
    return 15


def func2():
    return [23, 57, 80]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
