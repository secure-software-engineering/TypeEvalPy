# Functions are assigned to variables via starred assignment
def func1():
    return [24, 70, 72]


def func2():
    return 65


def func3():
    return 1.66


def func4():
    return 'aisem'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
