# A dictionary key is assigned to a function.


def func1():
    return {'zlztj': 39, 'vpycf': 30, 'smwgh': 12}


def func2():
    return 64.3


d = {"a": func1}

d["a"] = func2

e = d["a"]()
