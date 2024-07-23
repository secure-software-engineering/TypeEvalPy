# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 60.77


def func2():
    return (20, 53, 98)


x = lambda x: x()

a = x(func1)

b = x(func2)
