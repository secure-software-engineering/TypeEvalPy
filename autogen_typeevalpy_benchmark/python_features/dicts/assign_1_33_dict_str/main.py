# A dictionary key is assigned to a function.


def func1():
    return {'nrsmo': 55, 'nbtkz': 60, 'wtryw': 52}


def func2():
    return 'jjmfl'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
