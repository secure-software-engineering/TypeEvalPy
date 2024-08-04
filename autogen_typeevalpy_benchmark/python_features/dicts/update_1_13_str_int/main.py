# The update method of dictionaries is used.


def func1():
    return 71


def func2():
    return 'ildae'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
