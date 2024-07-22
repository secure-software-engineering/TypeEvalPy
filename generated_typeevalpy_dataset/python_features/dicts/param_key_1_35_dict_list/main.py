# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return {'rkucj': 91, 'idauz': 41, 'aonan': 67}


def func3():
    return [34, 41, 58]


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
