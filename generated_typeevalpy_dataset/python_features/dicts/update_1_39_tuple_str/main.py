# The update method of dictionaries is used.


def func1():
    return 'tolts'


def func2():
    return (6, 29, 75)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
