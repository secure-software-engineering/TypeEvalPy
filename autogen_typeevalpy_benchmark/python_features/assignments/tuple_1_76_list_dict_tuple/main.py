# Two variables are assigned a value via a tuple assignment.
def func1():
    return [84, 77, 7]


def func2():
    return {'smryu': 35, 'ivhwh': 56, 'uwzos': 82}


def func3():
    return (44, 64, 59)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
