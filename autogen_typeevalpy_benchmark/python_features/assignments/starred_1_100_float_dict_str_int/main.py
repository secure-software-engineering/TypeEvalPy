# Functions are assigned to variables via starred assignment
def func1():
    return 15.7


def func2():
    return {'apyek': 1, 'msrge': 7, 'goyzk': 63}


def func3():
    return 'lghob'


def func4():
    return 28

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
