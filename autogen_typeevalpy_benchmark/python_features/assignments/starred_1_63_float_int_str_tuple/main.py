# Functions are assigned to variables via starred assignment
def func1():
    return 18.21


def func2():
    return 99


def func3():
    return 'oftwr'


def func4():
    return (67, 16, 93)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
