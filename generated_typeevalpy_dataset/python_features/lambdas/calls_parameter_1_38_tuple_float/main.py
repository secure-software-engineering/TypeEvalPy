# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (78, 48, 50)


def func2():
    return 45.89


x = lambda x: x()

a = x(func1)

b = x(func2)
