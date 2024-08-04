# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (22, 61, 5)


def func2():
    return 13.93


x = lambda x: x()

a = x(func1)

b = x(func2)
