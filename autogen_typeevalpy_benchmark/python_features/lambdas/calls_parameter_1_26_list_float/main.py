# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [8, 32, 42]


def func2():
    return 32.74


x = lambda x: x()

a = x(func1)

b = x(func2)
