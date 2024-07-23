# The update method of dictionaries is used.


def func1():
    return 51


def func2():
    return [6, 38, 17]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
