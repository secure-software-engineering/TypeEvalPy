# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 24


def func2():
    return {'euflw': 19, 'bvdqx': 22, 'ibmji': 54}


x = lambda x: x()

a = x(func1)

b = x(func2)
