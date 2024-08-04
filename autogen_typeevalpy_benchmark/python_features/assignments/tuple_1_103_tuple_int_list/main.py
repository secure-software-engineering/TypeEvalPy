# Two variables are assigned a value via a tuple assignment.
def func1():
    return (85, 3, 44)


def func2():
    return 53


def func3():
    return [48, 81, 13]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
