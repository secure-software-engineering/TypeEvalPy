# A dictionary key is assigned to a function.


def func1():
    return {'txafa': 5, 'jjpop': 59, 'kapwt': 44}


def func2():
    return [16, 96, 75]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
