# A dictionary key is assigned to a function.


def func1():
    return {'rfsdv': 63, 'djjfn': 17, 'vmles': 7}


def func2():
    return 23.95


d = {"a": func1}

d["a"] = func2

e = d["a"]()
