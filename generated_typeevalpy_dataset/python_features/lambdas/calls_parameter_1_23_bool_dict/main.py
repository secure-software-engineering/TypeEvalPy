# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return False


def func2():
    return {'mlufi': 10, 'ngcjd': 27, 'ixmdg': 45}


x = lambda x: x()

a = x(func1)

b = x(func2)
