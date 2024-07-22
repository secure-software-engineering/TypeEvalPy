# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (58, 34, 3)


def func2():
    return [13, 78, 98]


x = lambda x: x()

a = x(func1)

b = x(func2)
