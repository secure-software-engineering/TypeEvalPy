# The update method of dictionaries is used.


def func1():
    return {'aoqqi': 47, 'pivig': 36, 'lkyhs': 78}


def func2():
    return True


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
