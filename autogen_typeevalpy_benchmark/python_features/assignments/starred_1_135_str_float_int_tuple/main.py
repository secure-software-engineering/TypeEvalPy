# Functions are assigned to variables via starred assignment
def func1():
    return 'ovmdg'


def func2():
    return 63.98


def func3():
    return 11


def func4():
    return (62, 42, 45)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
