# The update method of dictionaries is used.


def func1():
    return [56, 42, 32]


def func2():
    return 'seyyl'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
