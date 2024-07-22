# Two variables are assigned a value via a tuple assignment.
def func1():
    return (82, 90, 70)


def func2():
    return [23, 10, 18]


def func3():
    return 80.41


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
