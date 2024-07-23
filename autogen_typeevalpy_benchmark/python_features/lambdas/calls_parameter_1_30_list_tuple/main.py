# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [82, 94, 97]


def func2():
    return (13, 6, 83)


x = lambda x: x()

a = x(func1)

b = x(func2)
