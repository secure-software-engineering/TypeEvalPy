# Two variables are assigned a value via a tuple assignment.
def func1():
    return 96.06


def func2():
    return [56, 67, 75]


def func3():
    return (100, 11, 71)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
