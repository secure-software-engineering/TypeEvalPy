# The update method of dictionaries is used.


def func1():
    return [79, 46, 32]


def func2():
    return (27, 62, 32)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
