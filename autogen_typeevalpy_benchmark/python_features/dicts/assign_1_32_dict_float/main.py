# A dictionary key is assigned to a function.


def func1():
    return {'kfwyv': 31, 'vdzmc': 73, 'viqki': 7}


def func2():
    return 23.01


d = {"a": func1}

d["a"] = func2

e = d["a"]()
