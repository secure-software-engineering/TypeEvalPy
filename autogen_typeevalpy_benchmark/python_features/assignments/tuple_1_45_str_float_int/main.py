# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'kshui'


def func2():
    return 39.88


def func3():
    return 68


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
