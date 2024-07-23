# A dictionary key is assigned to a function.


def func1():
    return 41.09


def func2():
    return {'qwvps': 44, 'eeiux': 86, 'mjfei': 13}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
