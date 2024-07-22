# The update method of dictionaries is used.


def func1():
    return 45.79


def func2():
    return 'aikqe'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
