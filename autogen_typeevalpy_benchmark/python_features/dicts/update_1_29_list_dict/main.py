# The update method of dictionaries is used.


def func1():
    return {'wsmhe': 87, 'wpirj': 100, 'vzlxy': 34}


def func2():
    return [18, 5, 80]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
