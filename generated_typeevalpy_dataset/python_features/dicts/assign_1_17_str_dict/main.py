# A dictionary key is assigned to a function.


def func1():
    return 'nhdam'


def func2():
    return {'jcwfz': 3, 'sconn': 76, 'mfiqq': 74}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
