# A dictionary key is assigned to a function.


def func1():
    return {'qzrzu': 99, 'dxrap': 99, 'jztxp': 46}


def func2():
    return [67, 72, 89]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
