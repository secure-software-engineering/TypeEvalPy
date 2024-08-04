# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [14, 92, 18]


def func2():
    return (27, 75, 44)


x = lambda x: x()

a = x(func1)

b = x(func2)
