# Two variables are assigned a value via a tuple assignment.
def func1():
    return (52, 25, 33)


def func2():
    return 15.49


def func3():
    return {'fmxky': 30, 'utsdw': 75, 'curip': 65}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
