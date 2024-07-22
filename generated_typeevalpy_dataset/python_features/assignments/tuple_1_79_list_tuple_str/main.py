# Two variables are assigned a value via a tuple assignment.
def func1():
    return [96, 13, 86]


def func2():
    return (24, 71, 95)


def func3():
    return 'sgutj'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
