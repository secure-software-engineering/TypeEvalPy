# Functions are assigned to variables via starred assignment
def func1():
    return 25


def func2():
    return 45.03


def func3():
    return [94, 20, 89]


def func4():
    return 'bosis'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
