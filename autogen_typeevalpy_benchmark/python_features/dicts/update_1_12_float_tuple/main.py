# The update method of dictionaries is used.


def func1():
    return (62, 44, 43)


def func2():
    return 71.99


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
