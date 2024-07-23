# Functions are assigned to variables via starred assignment
def func1():
    return 31.71


def func2():
    return 99


def func3():
    return 'ifktp'


def func4():
    return (60, 64, 78)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
