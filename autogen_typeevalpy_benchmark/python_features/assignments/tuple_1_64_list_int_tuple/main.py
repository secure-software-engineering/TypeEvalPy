# Two variables are assigned a value via a tuple assignment.
def func1():
    return [48, 20, 97]


def func2():
    return 98


def func3():
    return (77, 93, 79)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
