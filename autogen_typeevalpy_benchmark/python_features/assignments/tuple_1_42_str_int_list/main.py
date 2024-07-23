# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'mgrys'


def func2():
    return 52


def func3():
    return [100, 65, 96]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
