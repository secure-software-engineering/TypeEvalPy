# Functions are assigned to variables via starred assignment
def func1():
    return 24.23


def func2():
    return [41, 40, 2]


def func3():
    return 13


def func4():
    return (70, 13, 84)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
