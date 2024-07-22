# Two variables are assigned a value via a tuple assignment.
def func1():
    return [43, 23, 73]


def func2():
    return 'saurk'


def func3():
    return 14


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
