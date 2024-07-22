# Functions are assigned to variables via starred assignment
def func1():
    return (11, 38, 54)


def func2():
    return 'pxhee'


def func3():
    return 38.85


def func4():
    return [100, 10, 34]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
