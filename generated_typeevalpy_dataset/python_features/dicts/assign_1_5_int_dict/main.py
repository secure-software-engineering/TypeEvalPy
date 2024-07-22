# A dictionary key is assigned to a function.


def func1():
    return 18


def func2():
    return {'aagkt': 6, 'riamv': 6, 'rsenq': 85}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
