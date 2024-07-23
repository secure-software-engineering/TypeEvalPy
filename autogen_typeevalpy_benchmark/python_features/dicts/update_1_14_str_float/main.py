# The update method of dictionaries is used.


def func1():
    return 54.27


def func2():
    return 'ufvlo'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
