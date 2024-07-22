# Two variables are assigned a value via a tuple assignment.
def func1():
    return (13, 41, 76)


def func2():
    return 9.61


def func3():
    return 'erfep'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
