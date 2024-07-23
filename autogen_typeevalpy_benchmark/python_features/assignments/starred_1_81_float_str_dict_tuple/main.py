# Functions are assigned to variables via starred assignment
def func1():
    return 91.38


def func2():
    return 'ttazq'


def func3():
    return {'fmlrk': 92, 'vvraj': 62, 'mhvom': 29}


def func4():
    return (95, 45, 84)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
