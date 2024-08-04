# The update method of dictionaries is used.


def func1():
    return [28, 43, 57]


def func2():
    return {'xihlq': 7, 'jzrxv': 88, 'nmlgx': 69}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
