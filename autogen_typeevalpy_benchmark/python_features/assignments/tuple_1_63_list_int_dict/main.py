# Two variables are assigned a value via a tuple assignment.
def func1():
    return [96, 68, 79]


def func2():
    return 51


def func3():
    return {'ifqia': 69, 'lvhwa': 48, 'znjnf': 52}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
