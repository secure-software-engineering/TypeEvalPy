# Two variables are assigned a value via a tuple assignment.
def func1():
    return [84, 47, 85]


def func2():
    return 36


def func3():
    return (70, 65, 38)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
