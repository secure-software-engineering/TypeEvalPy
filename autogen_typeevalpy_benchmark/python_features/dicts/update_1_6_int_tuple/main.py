# The update method of dictionaries is used.


def func1():
    return (84, 35, 13)


def func2():
    return 14


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
