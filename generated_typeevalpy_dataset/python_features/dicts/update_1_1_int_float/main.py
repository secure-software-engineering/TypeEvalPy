# The update method of dictionaries is used.


def func1():
    return 72.02


def func2():
    return 70


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
