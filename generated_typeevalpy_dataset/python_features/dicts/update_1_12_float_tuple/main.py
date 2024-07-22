# The update method of dictionaries is used.


def func1():
    return (62, 25, 53)


def func2():
    return 97.7


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
