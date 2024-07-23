# Two variables are assigned a value via a tuple assignment.
def func1():
    return (78, 38, 86)


def func2():
    return {'alzvi': 1, 'yezal': 3, 'pagzo': 31}


def func3():
    return 'rbpov'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
