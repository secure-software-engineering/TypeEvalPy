# A dictionary key is assigned to a function.


def func1():
    return 63.43


def func2():
    return {'mbnup': 58, 'ywzzm': 27, 'tegkf': 7}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
