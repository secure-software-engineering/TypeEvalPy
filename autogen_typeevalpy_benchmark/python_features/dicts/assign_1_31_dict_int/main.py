# A dictionary key is assigned to a function.


def func1():
    return {'xyxjo': 17, 'gljso': 8, 'kgfvp': 62}


def func2():
    return 29


d = {"a": func1}

d["a"] = func2

e = d["a"]()
