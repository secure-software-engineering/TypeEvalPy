# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 17.16


def func2():
    return {'kixmm': 5, 'lvxux': 85, 'ndsge': 82}


x = lambda x: x()

a = x(func1)

b = x(func2)
