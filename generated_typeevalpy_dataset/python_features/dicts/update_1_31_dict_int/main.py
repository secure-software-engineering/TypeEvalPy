# The update method of dictionaries is used.


def func1():
    return 69


def func2():
    return {'malhb': 73, 'ufaaq': 64, 'rwqkf': 12}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
