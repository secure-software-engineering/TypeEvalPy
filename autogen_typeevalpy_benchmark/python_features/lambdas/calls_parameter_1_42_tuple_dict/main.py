# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (8, 92, 86)


def func2():
    return {'sjwcs': 64, 'gmuyt': 9, 'rhfaj': 85}


x = lambda x: x()

a = x(func1)

b = x(func2)
