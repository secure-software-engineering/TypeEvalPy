# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [25, 44, 89]


def func2():
    return 25.64


x = lambda x: x()

a = x(func1)

b = x(func2)
