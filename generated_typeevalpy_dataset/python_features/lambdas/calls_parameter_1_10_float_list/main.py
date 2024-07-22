# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 38.06


def func2():
    return [88, 68, 90]


x = lambda x: x()

a = x(func1)

b = x(func2)
