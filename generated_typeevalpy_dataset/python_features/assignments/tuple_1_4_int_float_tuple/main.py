# Two variables are assigned a value via a tuple assignment.
def func1():
    return 59


def func2():
    return 65.56


def func3():
    return (89, 44, 11)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
