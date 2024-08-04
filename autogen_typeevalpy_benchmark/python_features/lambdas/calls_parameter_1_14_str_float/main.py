# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 'zejhv'


def func2():
    return 43.37


x = lambda x: x()

a = x(func1)

b = x(func2)
