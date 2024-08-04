# Two variables are assigned a value via a tuple assignment.
def func1():
    return 93


def func2():
    return 37.99


def func3():
    return 'wiort'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
