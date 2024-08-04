# Functions are assigned to variables via starred assignment
def func1():
    return 61.82


def func2():
    return 'qbewc'


def func3():
    return [16, 15, 36]


def func4():
    return 70

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
