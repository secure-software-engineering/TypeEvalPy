# The update method of dictionaries is used.


def func1():
    return 'zutyw'


def func2():
    return (28, 100, 56)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
