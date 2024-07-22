# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 60.29


def func2():
    return {'zifdd': 63, 'bcclb': 58, 'bgdle': 82}


x = lambda x: x()

a = x(func1)

b = x(func2)
