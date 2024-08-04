# The update method of dictionaries is used.


def func1():
    return 22.89


def func2():
    return [20, 66, 84]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
