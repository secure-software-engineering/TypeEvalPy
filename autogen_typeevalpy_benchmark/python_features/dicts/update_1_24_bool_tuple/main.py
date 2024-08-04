# The update method of dictionaries is used.


def func1():
    return (31, 47, 47)


def func2():
    return True


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
