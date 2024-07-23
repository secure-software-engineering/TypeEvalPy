# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return {'vcfjl': 24, 'cusfs': 80, 'hgect': 51}


def func3():
    return 27


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
