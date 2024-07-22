# Functions are assigned to variables via starred assignment
def func1():
    return 'rfnaj'


def func2():
    return 86.04


def func3():
    return (49, 51, 29)


def func4():
    return 1

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
