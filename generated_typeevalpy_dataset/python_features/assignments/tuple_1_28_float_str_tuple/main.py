# Two variables are assigned a value via a tuple assignment.
def func1():
    return 34.19


def func2():
    return 'huoyb'


def func3():
    return (46, 53, 52)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
