# Two variables are assigned a value via a tuple assignment.
def func1():
    return 91


def func2():
    return [50, 82, 14]


def func3():
    return (74, 98, 52)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
