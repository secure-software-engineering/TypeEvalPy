# The update method of dictionaries is used.


def func1():
    return 46.21


def func2():
    return (73, 62, 45)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
