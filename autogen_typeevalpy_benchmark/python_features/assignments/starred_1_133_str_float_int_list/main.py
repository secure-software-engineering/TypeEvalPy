# Functions are assigned to variables via starred assignment
def func1():
    return 'vnpht'


def func2():
    return 36.69


def func3():
    return 38


def func4():
    return [13, 75, 56]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
