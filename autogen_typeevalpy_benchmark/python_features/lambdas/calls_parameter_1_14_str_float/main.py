# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 'cuevq'


def func2():
    return 19.27


x = lambda x: x()

a = x(func1)

b = x(func2)
