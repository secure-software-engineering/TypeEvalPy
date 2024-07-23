# The update method of dictionaries is used.


def func1():
    return 49.36


def func2():
    return (89, 95, 88)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
