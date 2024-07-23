# The update method of dictionaries is used.


def func1():
    return 66


def func2():
    return 'glbil'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
