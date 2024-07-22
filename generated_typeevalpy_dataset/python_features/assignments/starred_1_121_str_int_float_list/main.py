# Functions are assigned to variables via starred assignment
def func1():
    return 'uaxwy'


def func2():
    return 84


def func3():
    return 20.11


def func4():
    return [70, 6, 49]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
