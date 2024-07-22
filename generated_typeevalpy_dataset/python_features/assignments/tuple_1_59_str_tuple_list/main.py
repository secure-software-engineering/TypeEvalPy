# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'sirmm'


def func2():
    return (93, 26, 52)


def func3():
    return [20, 78, 16]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
