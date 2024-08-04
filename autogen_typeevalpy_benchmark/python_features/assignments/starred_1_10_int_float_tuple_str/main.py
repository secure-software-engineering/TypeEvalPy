# Functions are assigned to variables via starred assignment
def func1():
    return 10


def func2():
    return 69.02


def func3():
    return (43, 25, 67)


def func4():
    return 'qcnfi'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
