# Two variables are assigned a value via a tuple assignment.
def func1():
    return (57, 66, 35)


def func2():
    return [31, 84, 50]


def func3():
    return 68.65


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
