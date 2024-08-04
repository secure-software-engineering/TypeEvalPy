# The update method of dictionaries is used.


def func1():
    return [68, 1, 85]


def func2():
    return 2.39


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
