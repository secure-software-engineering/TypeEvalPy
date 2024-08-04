# Two variables are assigned a value via a tuple assignment.
def func1():
    return [75, 25, 24]


def func2():
    return 93


def func3():
    return (78, 16, 32)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
