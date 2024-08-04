# Functions are assigned to variables via starred assignment
def func1():
    return {'gdqpl': 9, 'expbw': 92, 'lagfp': 74}


def func2():
    return 94


def func3():
    return 23.58


def func4():
    return 'eiunx'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
