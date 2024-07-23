# Functions are assigned to variables via starred assignment
def func1():
    return {'gvkhi': 50, 'vnotd': 3, 'pdrwm': 20}


def func2():
    return 'gkidk'


def func3():
    return 60.67


def func4():
    return 61

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
