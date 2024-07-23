# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return True


def func2():
    return 91


x = lambda x: x()

a = x(func1)

b = x(func2)
