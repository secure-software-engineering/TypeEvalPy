# The update method of dictionaries is used.


def func1():
    return (50, 83, 65)


def func2():
    return 42


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
