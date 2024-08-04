# Functions are assigned to variables via starred assignment
def func1():
    return 10.58


def func2():
    return 39


def func3():
    return (23, 81, 86)


def func4():
    return 'cenck'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
