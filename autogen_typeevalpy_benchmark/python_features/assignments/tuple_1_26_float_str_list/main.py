# Two variables are assigned a value via a tuple assignment.
def func1():
    return 73.23


def func2():
    return 'phgie'


def func3():
    return [65, 96, 97]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
