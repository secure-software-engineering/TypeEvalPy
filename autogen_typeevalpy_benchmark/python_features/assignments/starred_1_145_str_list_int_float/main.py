# Functions are assigned to variables via starred assignment
def func1():
    return 'onfcc'


def func2():
    return [23, 79, 86]


def func3():
    return 58


def func4():
    return 40.22

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
