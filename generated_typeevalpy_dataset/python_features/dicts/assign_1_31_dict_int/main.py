# A dictionary key is assigned to a function.


def func1():
    return {'xodsn': 33, 'hxcwo': 69, 'zojaa': 19}


def func2():
    return 19


d = {"a": func1}

d["a"] = func2

e = d["a"]()
