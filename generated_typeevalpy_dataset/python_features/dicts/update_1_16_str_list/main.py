# The update method of dictionaries is used.


def func1():
    return [28, 49, 31]


def func2():
    return 'bfuuk'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
