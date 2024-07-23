# The update method of dictionaries is used.


def func1():
    return 88


def func2():
    return {'vdzag': 49, 'vwwxk': 16, 'epsxg': 28}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
