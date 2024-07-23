# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'zedxw'


def func2():
    return 12.11


def func3():
    return (99, 50, 27)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
