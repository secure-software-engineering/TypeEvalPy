# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 'ghbfd'


def func2():
    return [79, 81, 41]


x = lambda x: x()

a = x(func1)

b = x(func2)
