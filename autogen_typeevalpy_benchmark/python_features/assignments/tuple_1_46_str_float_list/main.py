# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'wxsjp'


def func2():
    return 84.01


def func3():
    return [73, 22, 85]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
