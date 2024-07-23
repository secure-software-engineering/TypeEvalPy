# Functions are assigned to variables via starred assignment
def func1():
    return 36


def func2():
    return 70.35


def func3():
    return [6, 65, 77]


def func4():
    return 'smgnt'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
