# Two variables are assigned a value via a tuple assignment.
def func1():
    return (52, 51, 86)


def func2():
    return 52


def func3():
    return {'fjzlo': 69, 'hybdm': 46, 'gemlk': 90}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
