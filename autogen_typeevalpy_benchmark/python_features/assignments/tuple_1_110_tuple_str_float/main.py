# Two variables are assigned a value via a tuple assignment.
def func1():
    return (42, 57, 72)


def func2():
    return 'bfrou'


def func3():
    return 10.35


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
