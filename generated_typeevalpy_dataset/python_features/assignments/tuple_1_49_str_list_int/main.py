# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'kfbyk'


def func2():
    return [9, 74, 34]


def func3():
    return 40


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
