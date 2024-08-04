# Two variables are assigned a value via a tuple assignment.
def func1():
    return 99


def func2():
    return (93, 70, 52)


def func3():
    return {'ltinh': 64, 'ywpqu': 96, 'kqdje': 63}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
