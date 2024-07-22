# Two variables are assigned a value via a tuple assignment.
def func1():
    return 24.84


def func2():
    return [77, 74, 8]


def func3():
    return (95, 52, 100)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
