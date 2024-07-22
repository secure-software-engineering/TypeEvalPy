# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return 51.57


def func3():
    return {'erusy': 17, 'fddwi': 24, 'vlzdw': 29}


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
