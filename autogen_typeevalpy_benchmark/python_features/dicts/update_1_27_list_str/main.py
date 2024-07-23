# The update method of dictionaries is used.


def func1():
    return 'vdpya'


def func2():
    return [83, 2, 83]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
