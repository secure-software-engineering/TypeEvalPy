# The update method of dictionaries is used.


def func1():
    return 96


def func2():
    return 10.88


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
