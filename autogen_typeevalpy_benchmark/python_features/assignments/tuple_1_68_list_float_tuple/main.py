# Two variables are assigned a value via a tuple assignment.
def func1():
    return [8, 2, 18]


def func2():
    return 1.59


def func3():
    return (58, 78, 56)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
