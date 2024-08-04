# The update method of dictionaries is used.


def func1():
    return {'ywjsl': 23, 'jznnr': 44, 'izmfb': 46}


def func2():
    return (53, 72, 42)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
