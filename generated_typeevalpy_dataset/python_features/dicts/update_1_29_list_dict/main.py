# The update method of dictionaries is used.


def func1():
    return {'whbdt': 47, 'dlppi': 14, 'chpfb': 42}


def func2():
    return [30, 4, 30]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
