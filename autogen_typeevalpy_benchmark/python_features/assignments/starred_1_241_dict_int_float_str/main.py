# Functions are assigned to variables via starred assignment
def func1():
    return {'zjolp': 86, 'mwkfg': 73, 'eulfq': 88}


def func2():
    return 87


def func3():
    return 54.03


def func4():
    return 'qfgkg'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
