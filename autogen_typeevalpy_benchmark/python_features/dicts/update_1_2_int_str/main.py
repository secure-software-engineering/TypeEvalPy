# The update method of dictionaries is used.


def func1():
    return 'cqpcr'


def func2():
    return 34


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
