# Functions are assigned to variables via starred assignment
def func1():
    return 32


def func2():
    return (78, 39, 42)


def func3():
    return {'ouswu': 73, 'uzysq': 41, 'rmwnp': 69}


def func4():
    return 'ppegb'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
