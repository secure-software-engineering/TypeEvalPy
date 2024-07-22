# Functions are assigned to variables via starred assignment
def func1():
    return 'vjdio'


def func2():
    return 84.07


def func3():
    return {'cdiox': 16, 'upbvx': 84, 'irlex': 32}


def func4():
    return (52, 54, 95)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
