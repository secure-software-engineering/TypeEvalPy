# Two variables are assigned a value via a tuple assignment.
def func1():
    return 96.06


def func2():
    return (64, 19, 26)


def func3():
    return [12, 47, 41]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
