# The update method of dictionaries is used.


def func1():
    return 55.89


def func2():
    return 'wiekz'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
