# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return 1.58


def func3():
    return {'oeoql': 50, 'nremb': 42, 'pkznv': 88}


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
