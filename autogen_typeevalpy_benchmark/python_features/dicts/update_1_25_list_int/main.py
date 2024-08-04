# The update method of dictionaries is used.


def func1():
    return 59


def func2():
    return [68, 65, 45]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
