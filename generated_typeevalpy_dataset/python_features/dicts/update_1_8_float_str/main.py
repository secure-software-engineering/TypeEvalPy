# The update method of dictionaries is used.


def func1():
    return 'biwua'


def func2():
    return 53.77


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
