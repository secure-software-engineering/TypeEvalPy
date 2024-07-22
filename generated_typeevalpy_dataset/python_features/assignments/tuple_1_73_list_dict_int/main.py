# Two variables are assigned a value via a tuple assignment.
def func1():
    return [40, 52, 20]


def func2():
    return {'qxcyo': 78, 'nzdkx': 50, 'zuztn': 80}


def func3():
    return 40


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
