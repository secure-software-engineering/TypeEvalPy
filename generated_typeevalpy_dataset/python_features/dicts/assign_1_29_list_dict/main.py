# A dictionary key is assigned to a function.


def func1():
    return [92, 24, 80]


def func2():
    return {'gaeve': 54, 'uwatf': 52, 'ipibq': 29}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
