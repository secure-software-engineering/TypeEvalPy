# Two variables are assigned a value via a tuple assignment.
def func1():
    return 91.41


def func2():
    return [41, 47, 88]


def func3():
    return 'rrnna'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
