# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [17, 18, 73]


def func2():
    return (17, 30, 2)


x = lambda x: x()

a = x(func1)

b = x(func2)
