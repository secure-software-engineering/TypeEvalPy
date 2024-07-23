# The update method of dictionaries is used.


def func1():
    return 7.43


def func2():
    return [68, 94, 7]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
