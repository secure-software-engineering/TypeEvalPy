# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [41, 69, 26]


def func2():
    return 84


x = lambda x: x()

a = x(func1)

b = x(func2)
