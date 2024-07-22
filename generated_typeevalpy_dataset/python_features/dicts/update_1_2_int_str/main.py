# The update method of dictionaries is used.


def func1():
    return 'wbgov'


def func2():
    return 70


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
