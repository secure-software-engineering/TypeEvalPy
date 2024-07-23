# The update method of dictionaries is used.


def func1():
    return [97, 50, 55]


def func2():
    return {'uinza': 8, 'rvfen': 50, 'ambwx': 17}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
