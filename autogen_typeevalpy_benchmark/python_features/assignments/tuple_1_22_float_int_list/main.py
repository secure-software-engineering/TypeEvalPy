# Two variables are assigned a value via a tuple assignment.
def func1():
    return 21.42


def func2():
    return 92


def func3():
    return [19, 42, 19]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
