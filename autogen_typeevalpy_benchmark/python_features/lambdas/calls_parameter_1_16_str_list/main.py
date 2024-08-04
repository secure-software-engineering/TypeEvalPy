# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 'nfwpq'


def func2():
    return [69, 83, 77]


x = lambda x: x()

a = x(func1)

b = x(func2)
