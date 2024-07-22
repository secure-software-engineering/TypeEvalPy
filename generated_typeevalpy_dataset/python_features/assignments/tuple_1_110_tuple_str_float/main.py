# Two variables are assigned a value via a tuple assignment.
def func1():
    return (1, 21, 37)


def func2():
    return 'tysjm'


def func3():
    return 20.34


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
