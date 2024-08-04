# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return {'upbmh': 33, 'pqvxg': 100, 'zeedq': 35}


def func3():
    return (2, 88, 62)


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
