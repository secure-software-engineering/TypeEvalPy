# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 83.85


def func2():
    return 'lkugb'


x = lambda x: x()

a = x(func1)

b = x(func2)
