# The update method of dictionaries is used.


def func1():
    return {'xzqkb': 36, 'ihofv': 89, 'bdmbt': 70}


def func2():
    return (40, 50, 88)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
