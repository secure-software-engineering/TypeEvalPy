# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'dkioo'


def func2():
    return 29.78


def func3():
    return [50, 87, 81]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
