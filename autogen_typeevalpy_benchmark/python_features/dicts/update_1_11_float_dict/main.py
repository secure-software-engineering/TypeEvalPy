# The update method of dictionaries is used.


def func1():
    return {'ufbee': 51, 'drrop': 94, 'gczzu': 95}


def func2():
    return 16.44


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
