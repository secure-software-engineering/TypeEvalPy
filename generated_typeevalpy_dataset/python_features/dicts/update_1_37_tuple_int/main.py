# The update method of dictionaries is used.


def func1():
    return 95


def func2():
    return (85, 84, 65)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
