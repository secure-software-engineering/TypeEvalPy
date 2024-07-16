# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return <value1>


def func2():
    return <value2>


x = lambda x: x()

a = x(func1)

b = x(func2)
