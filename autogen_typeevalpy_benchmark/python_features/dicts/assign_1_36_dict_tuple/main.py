# A dictionary key is assigned to a function.


def func1():
    return {'ykxmj': 78, 'akxqr': 87, 'rxqhf': 56}


def func2():
    return (45, 55, 69)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
