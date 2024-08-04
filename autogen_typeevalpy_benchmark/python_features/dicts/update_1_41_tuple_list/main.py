# The update method of dictionaries is used.


def func1():
    return [18, 43, 66]


def func2():
    return (94, 46, 45)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
