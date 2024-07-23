# The update method of dictionaries is used.


def func1():
    return 12


def func2():
    return (38, 90, 3)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
