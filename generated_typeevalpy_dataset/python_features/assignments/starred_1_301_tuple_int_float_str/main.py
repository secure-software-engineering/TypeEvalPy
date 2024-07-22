# Functions are assigned to variables via starred assignment
def func1():
    return (84, 97, 47)


def func2():
    return 30


def func3():
    return 61.48


def func4():
    return 'oelqt'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
