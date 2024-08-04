# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return {'qafec': 44, 'nqlnv': 85, 'bpwra': 17}


def func3():
    return [6, 33, 52]


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
