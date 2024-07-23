# Two variables are assigned a value via a tuple assignment.
def func1():
    return (31, 41, 57)


def func2():
    return 40.67


def func3():
    return 'pdsza'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
