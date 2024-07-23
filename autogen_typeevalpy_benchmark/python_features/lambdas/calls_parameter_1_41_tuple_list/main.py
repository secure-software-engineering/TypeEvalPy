# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (21, 40, 17)


def func2():
    return [62, 11, 59]


x = lambda x: x()

a = x(func1)

b = x(func2)
