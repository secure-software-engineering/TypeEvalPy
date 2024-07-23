# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'dfzrt'


def func2():
    return [98, 69, 93]


def func3():
    return 59.82


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
