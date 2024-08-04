# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'onqot'


def func2():
    return (5, 97, 68)


def func3():
    return 44


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
