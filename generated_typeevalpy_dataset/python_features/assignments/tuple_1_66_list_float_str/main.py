# Two variables are assigned a value via a tuple assignment.
def func1():
    return [41, 23, 72]


def func2():
    return 67.1


def func3():
    return 'gwmuh'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
