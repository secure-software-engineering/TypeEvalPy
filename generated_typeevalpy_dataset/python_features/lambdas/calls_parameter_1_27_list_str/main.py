# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [53, 27, 62]


def func2():
    return 'ymktf'


x = lambda x: x()

a = x(func1)

b = x(func2)
