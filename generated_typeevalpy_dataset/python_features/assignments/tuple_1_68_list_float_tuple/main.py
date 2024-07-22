# Two variables are assigned a value via a tuple assignment.
def func1():
    return [3, 99, 11]


def func2():
    return 59.54


def func3():
    return (26, 14, 16)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
