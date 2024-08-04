# Two variables are assigned a value via a tuple assignment.
def func1():
    return 59.58


def func2():
    return 'orhtc'


def func3():
    return (15, 55, 68)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
