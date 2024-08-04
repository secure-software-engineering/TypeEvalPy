# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 96.57


def func2():
    return 'vifym'


x = lambda x: x()

a = x(func1)

b = x(func2)
