# The update method of dictionaries is used.


def func1():
    return (87, 34, 60)


def func2():
    return 58


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
