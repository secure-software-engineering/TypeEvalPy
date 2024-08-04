# A dictionary key is assigned to a function.


def func1():
    return 88.56


def func2():
    return {'acpey': 35, 'sauka': 27, 'qzrhu': 63}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
