# Two variables are assigned a value via a tuple assignment.
def func1():
    return [5, 32, 28]


def func2():
    return 'wyxfu'


def func3():
    return 80


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
