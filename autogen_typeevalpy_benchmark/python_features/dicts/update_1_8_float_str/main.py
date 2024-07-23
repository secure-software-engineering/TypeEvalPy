# The update method of dictionaries is used.


def func1():
    return 'kswsh'


def func2():
    return 67.34


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
