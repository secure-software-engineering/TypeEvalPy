# The update method of dictionaries is used.


def func1():
    return 6


def func2():
    return {'scigo': 76, 'voqdq': 33, 'ninnm': 6}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
