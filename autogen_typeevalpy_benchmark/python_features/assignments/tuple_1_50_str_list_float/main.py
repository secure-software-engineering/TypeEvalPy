# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'crspy'


def func2():
    return [95, 71, 81]


def func3():
    return 71.27


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
