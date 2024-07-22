# The update method of dictionaries is used.


def func1():
    return (1, 32, 92)


def func2():
    return [44, 55, 71]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
