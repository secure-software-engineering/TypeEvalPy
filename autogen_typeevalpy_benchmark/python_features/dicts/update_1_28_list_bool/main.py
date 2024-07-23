# The update method of dictionaries is used.


def func1():
    return True


def func2():
    return [7, 53, 53]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
