# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return {'skmws': 40, 'dtbjh': 78, 'vumxp': 26}


def func3():
    return 4.09


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
