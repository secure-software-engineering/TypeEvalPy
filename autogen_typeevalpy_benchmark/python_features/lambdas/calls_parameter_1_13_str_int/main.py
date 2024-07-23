# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 'jzeyu'


def func2():
    return 46


x = lambda x: x()

a = x(func1)

b = x(func2)
