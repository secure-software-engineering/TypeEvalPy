# A dictionary key is assigned to a function.


def func1():
    return (19, 93, 91)


def func2():
    return {'wmrpl': 3, 'hfwjj': 55, 'aobdq': 93}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
