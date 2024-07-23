# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 99


def func2():
    return {'htiob': 92, 'afets': 28, 'nulsb': 50}


x = lambda x: x()

a = x(func1)

b = x(func2)
