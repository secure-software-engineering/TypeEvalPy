# The update method of dictionaries is used.


def func1():
    return {'qbtel': 83, 'bwbto': 51, 'eewpj': 22}


def func2():
    return 'wtqur'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
