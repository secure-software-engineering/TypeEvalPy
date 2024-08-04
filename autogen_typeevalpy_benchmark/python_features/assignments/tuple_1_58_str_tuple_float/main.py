# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'rmynz'


def func2():
    return (62, 76, 38)


def func3():
    return 83.1


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
