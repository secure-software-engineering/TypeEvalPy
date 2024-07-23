# The update method of dictionaries is used.


def func1():
    return 51.23


def func2():
    return 44


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
