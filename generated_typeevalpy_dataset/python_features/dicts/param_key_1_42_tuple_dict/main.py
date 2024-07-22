# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return (13, 60, 91)


def func3():
    return {'ypcpw': 60, 'qecth': 25, 'rrksd': 83}


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
