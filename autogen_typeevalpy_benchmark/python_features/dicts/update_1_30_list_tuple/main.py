# The update method of dictionaries is used.


def func1():
    return (66, 79, 88)


def func2():
    return [60, 77, 100]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
