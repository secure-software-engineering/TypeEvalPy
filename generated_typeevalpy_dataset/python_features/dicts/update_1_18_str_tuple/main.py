# The update method of dictionaries is used.


def func1():
    return (19, 64, 82)


def func2():
    return 'cidpr'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
