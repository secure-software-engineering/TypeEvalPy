# Functions are assigned to variables via starred assignment
def func1():
    return [40, 70, 27]


def func2():
    return 73


def func3():
    return 'pfxky'


def func4():
    return 70.04

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
