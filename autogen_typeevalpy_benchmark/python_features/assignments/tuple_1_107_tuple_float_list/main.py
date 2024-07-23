# Two variables are assigned a value via a tuple assignment.
def func1():
    return (25, 26, 28)


def func2():
    return 10.43


def func3():
    return [51, 98, 37]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
