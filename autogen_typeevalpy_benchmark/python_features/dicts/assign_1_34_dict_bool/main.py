# A dictionary key is assigned to a function.


def func1():
    return {'ahove': 7, 'fejzh': 12, 'ttfoz': 7}


def func2():
    return True


d = {"a": func1}

d["a"] = func2

e = d["a"]()
