# Functions are assigned to variables via starred assignment
def func1():
    return 'fenxr'


def func2():
    return 89


def func3():
    return 7.14


def func4():
    return (93, 38, 1)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
