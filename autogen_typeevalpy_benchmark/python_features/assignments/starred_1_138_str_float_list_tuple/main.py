# Functions are assigned to variables via starred assignment
def func1():
    return 'dxdcq'


def func2():
    return 81.79


def func3():
    return [14, 80, 98]


def func4():
    return (67, 41, 29)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
