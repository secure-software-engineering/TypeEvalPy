# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [88, 9, 11]


def func2():
    return {'lksqz': 49, 'wqckj': 93, 'bgfvq': 61}


x = lambda x: x()

a = x(func1)

b = x(func2)
