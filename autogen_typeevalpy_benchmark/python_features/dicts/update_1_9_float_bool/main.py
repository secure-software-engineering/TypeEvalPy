# The update method of dictionaries is used.


def func1():
    return False


def func2():
    return 57.42


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
