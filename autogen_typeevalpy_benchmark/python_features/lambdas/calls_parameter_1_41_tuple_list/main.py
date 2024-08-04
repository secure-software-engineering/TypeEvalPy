# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (28, 9, 12)


def func2():
    return [50, 21, 9]


x = lambda x: x()

a = x(func1)

b = x(func2)
