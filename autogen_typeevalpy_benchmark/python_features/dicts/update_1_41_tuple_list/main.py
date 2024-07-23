# The update method of dictionaries is used.


def func1():
    return [90, 39, 86]


def func2():
    return (82, 99, 73)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
