# Two variables are assigned a value via a tuple assignment.
def func1():
    return (33, 98, 12)


def func2():
    return [3, 95, 4]


def func3():
    return 'iahbz'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
