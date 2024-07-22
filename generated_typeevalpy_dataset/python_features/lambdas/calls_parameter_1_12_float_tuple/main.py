# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 75.46


def func2():
    return (37, 55, 47)


x = lambda x: x()

a = x(func1)

b = x(func2)
