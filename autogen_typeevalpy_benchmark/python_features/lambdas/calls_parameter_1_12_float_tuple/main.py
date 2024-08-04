# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 29.81


def func2():
    return (9, 78, 79)


x = lambda x: x()

a = x(func1)

b = x(func2)
