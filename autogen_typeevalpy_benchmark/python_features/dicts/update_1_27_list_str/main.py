# The update method of dictionaries is used.


def func1():
    return 'qvclr'


def func2():
    return [52, 84, 28]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
