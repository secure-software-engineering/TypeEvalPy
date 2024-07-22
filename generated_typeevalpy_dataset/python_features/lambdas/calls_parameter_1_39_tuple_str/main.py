# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (91, 7, 63)


def func2():
    return 'hepkc'


x = lambda x: x()

a = x(func1)

b = x(func2)
