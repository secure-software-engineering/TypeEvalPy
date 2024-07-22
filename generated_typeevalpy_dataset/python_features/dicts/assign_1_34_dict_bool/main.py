# A dictionary key is assigned to a function.


def func1():
    return {'lbbdb': 83, 'agazp': 45, 'esxgv': 22}


def func2():
    return False


d = {"a": func1}

d["a"] = func2

e = d["a"]()
