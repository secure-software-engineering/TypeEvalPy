# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'ppflw': 77, 'gcctw': 39, 'mpwbw': 21}


def func2():
    return (18, 58, 55)


x = lambda x: x()

a = x(func1)

b = x(func2)
