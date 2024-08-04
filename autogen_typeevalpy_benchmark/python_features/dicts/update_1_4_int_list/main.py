# The update method of dictionaries is used.


def func1():
    return [73, 83, 85]


def func2():
    return 29


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
