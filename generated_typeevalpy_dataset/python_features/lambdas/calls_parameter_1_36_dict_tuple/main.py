# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'lktor': 22, 'ksynp': 24, 'grdyq': 70}


def func2():
    return (41, 86, 44)


x = lambda x: x()

a = x(func1)

b = x(func2)
