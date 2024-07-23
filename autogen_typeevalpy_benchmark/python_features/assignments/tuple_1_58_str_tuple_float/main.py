# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'aeueh'


def func2():
    return (43, 87, 64)


def func3():
    return 33.75


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
