# Functions are assigned to variables via starred assignment
def func1():
    return 47.69


def func2():
    return 93


def func3():
    return {'ijvom': 48, 'dvaib': 68, 'otpkr': 91}


def func4():
    return 'blujb'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
