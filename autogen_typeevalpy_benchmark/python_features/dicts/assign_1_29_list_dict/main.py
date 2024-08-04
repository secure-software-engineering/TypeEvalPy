# A dictionary key is assigned to a function.


def func1():
    return [11, 91, 31]


def func2():
    return {'vamdm': 45, 'atjso': 30, 'olvfr': 31}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
