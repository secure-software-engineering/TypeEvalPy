# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return 'uproz'


def func3():
    return {'eonju': 6, 'akdvl': 27, 'pqoum': 20}


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
