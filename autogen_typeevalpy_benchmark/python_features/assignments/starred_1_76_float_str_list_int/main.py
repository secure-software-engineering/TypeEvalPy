# Functions are assigned to variables via starred assignment
def func1():
    return 81.45


def func2():
    return 'yrwtl'


def func3():
    return [78, 11, 67]


def func4():
    return 9

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
