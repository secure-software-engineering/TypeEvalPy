# Two variables are assigned a value via a tuple assignment.
def func1():
    return [94, 26, 4]


def func2():
    return {'ulfgm': 41, 'mhsph': 5, 'nxyxe': 72}


def func3():
    return 65


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
