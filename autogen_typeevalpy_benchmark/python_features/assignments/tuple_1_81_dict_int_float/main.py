# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'jzzap': 81, 'puhub': 78, 'emyad': 46}


def func2():
    return 28


def func3():
    return 10.25


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
