# Functions are assigned to variables via starred assignment
def func1():
    return {'fgqtz': 45, 'mbkyr': 3, 'nkjxj': 7}


def func2():
    return 24


def func3():
    return [15, 76, 75]


def func4():
    return 'cthnr'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
