# The update method of dictionaries is used.


def func1():
    return 7


def func2():
    return 'sojai'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
