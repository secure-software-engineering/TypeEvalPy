# Two variables are assigned a value via a tuple assignment.
def func1():
    return 52


def func2():
    return [94, 100, 21]


def func3():
    return (37, 17, 70)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
