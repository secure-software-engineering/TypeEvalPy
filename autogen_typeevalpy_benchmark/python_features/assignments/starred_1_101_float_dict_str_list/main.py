# Functions are assigned to variables via starred assignment
def func1():
    return 51.9


def func2():
    return {'uqtgq': 3, 'otkob': 99, 'kijav': 11}


def func3():
    return 'wdoji'


def func4():
    return [79, 84, 27]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
