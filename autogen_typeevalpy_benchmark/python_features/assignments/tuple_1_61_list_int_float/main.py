# Two variables are assigned a value via a tuple assignment.
def func1():
    return [83, 5, 92]


def func2():
    return 82


def func3():
    return 13.84


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
