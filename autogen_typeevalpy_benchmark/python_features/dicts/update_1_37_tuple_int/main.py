# The update method of dictionaries is used.


def func1():
    return 100


def func2():
    return (25, 2, 41)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
