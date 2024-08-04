# The update method of dictionaries is used.


def func1():
    return (75, 72, 8)


def func2():
    return 'cgjzb'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
