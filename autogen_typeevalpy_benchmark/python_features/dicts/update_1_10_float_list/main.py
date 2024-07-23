# The update method of dictionaries is used.


def func1():
    return [55, 16, 47]


def func2():
    return 76.53


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
