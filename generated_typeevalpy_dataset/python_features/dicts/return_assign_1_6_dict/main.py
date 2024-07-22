# A dictionary key is assigned to the returned value of a function.


def func2():
    return {'xglqi': 82, 'fsbft': 33, 'iteaq': 37}


def func1():
    return func2


d = {"a": func1()}

e = d["a"]()
