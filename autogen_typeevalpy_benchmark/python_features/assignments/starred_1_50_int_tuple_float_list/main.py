# Functions are assigned to variables via starred assignment
def func1():
    return 28


def func2():
    return (52, 16, 63)


def func3():
    return 62.39


def func4():
    return [18, 58, 61]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
