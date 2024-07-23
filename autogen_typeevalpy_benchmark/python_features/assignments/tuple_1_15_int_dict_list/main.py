# Two variables are assigned a value via a tuple assignment.
def func1():
    return 70


def func2():
    return {'ivzet': 67, 'dhokx': 56, 'tcgbd': 77}


def func3():
    return [24, 14, 66]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
