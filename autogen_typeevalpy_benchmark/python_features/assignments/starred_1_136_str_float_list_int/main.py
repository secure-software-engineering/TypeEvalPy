# Functions are assigned to variables via starred assignment
def func1():
    return 'gkone'


def func2():
    return 79.76


def func3():
    return [28, 60, 98]


def func4():
    return 36

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
