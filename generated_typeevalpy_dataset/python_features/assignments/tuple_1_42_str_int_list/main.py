# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'ykron'


def func2():
    return 24


def func3():
    return [2, 18, 54]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
