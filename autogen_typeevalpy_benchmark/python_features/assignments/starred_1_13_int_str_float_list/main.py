# Functions are assigned to variables via starred assignment
def func1():
    return 28


def func2():
    return 'orupm'


def func3():
    return 91.89


def func4():
    return [13, 87, 67]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
