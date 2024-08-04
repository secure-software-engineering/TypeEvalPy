# A dictionary key is assigned to a function.


def func1():
    return 2


def func2():
    return {'hensu': 41, 'cbkea': 81, 'jiytx': 5}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
