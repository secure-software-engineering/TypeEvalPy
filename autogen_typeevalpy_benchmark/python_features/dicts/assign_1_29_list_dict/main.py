# A dictionary key is assigned to a function.


def func1():
    return [42, 62, 67]


def func2():
    return {'jxlif': 60, 'dapqk': 78, 'rqila': 24}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
