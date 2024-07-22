# The update method of dictionaries is used.


def func1():
    return 16.22


def func2():
    return [62, 8, 92]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
