# A dictionary key is assigned to a function.


def func1():
    return 93


def func2():
    return {'nblvf': 26, 'cjsww': 93, 'elivm': 93}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
