# Functions are assigned to variables via starred assignment
def func1():
    return 52.86


def func2():
    return [65, 96, 14]


def func3():
    return 40


def func4():
    return 'ulhmr'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
