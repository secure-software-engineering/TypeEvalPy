# Functions are assigned to variables via starred assignment
def func1():
    return 40.65


def func2():
    return [9, 9, 27]


def func3():
    return 28


def func4():
    return 'zmylm'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
