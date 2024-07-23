# The update method of dictionaries is used.


def func1():
    return {'slcux': 71, 'zfdpp': 94, 'pvseh': 73}


def func2():
    return 97


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
