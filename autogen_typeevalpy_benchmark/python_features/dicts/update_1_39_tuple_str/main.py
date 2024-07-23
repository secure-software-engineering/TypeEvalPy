# The update method of dictionaries is used.


def func1():
    return 'rllmn'


def func2():
    return (77, 80, 93)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
