# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return [85, 39, 9]


def func3():
    return {'lrsvn': 39, 'hxoss': 21, 'ljuji': 24}


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
