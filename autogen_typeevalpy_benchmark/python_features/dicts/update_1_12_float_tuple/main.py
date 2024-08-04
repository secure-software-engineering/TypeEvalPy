# The update method of dictionaries is used.


def func1():
    return (17, 54, 82)


def func2():
    return 25.93


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
