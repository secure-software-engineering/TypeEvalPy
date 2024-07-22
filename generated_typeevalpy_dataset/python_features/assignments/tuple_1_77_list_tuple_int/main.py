# Two variables are assigned a value via a tuple assignment.
def func1():
    return [77, 50, 45]


def func2():
    return (8, 3, 32)


def func3():
    return 88


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
