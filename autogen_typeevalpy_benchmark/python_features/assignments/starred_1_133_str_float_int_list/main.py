# Functions are assigned to variables via starred assignment
def func1():
    return 'rpeuy'


def func2():
    return 53.94


def func3():
    return 24


def func4():
    return [21, 68, 22]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
