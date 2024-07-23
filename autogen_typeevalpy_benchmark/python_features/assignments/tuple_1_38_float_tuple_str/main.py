# Two variables are assigned a value via a tuple assignment.
def func1():
    return 54.07


def func2():
    return (97, 99, 3)


def func3():
    return 'moegj'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
