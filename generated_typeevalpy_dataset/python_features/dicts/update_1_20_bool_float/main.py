# The update method of dictionaries is used.


def func1():
    return 3.92


def func2():
    return False


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
