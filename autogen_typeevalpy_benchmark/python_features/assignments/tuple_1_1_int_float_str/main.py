# Two variables are assigned a value via a tuple assignment.
def func1():
    return 79


def func2():
    return 79.77


def func3():
    return 'tgguh'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
