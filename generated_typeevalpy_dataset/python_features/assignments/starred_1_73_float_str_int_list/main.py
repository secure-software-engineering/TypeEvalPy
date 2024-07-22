# Functions are assigned to variables via starred assignment
def func1():
    return 7.24


def func2():
    return 'qucdb'


def func3():
    return 64


def func4():
    return [4, 32, 25]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
