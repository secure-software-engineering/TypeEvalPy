# The update method of dictionaries is used.


def func1():
    return (94, 66, 69)


def func2():
    return [84, 84, 25]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
