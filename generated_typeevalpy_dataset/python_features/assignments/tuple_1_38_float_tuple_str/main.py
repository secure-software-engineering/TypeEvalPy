# Two variables are assigned a value via a tuple assignment.
def func1():
    return 22.1


def func2():
    return (14, 77, 31)


def func3():
    return 'miunh'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
