# Functions are assigned to variables via starred assignment
def func1():
    return 71.64


def func2():
    return (23, 100, 27)


def func3():
    return 'jdxrg'


def func4():
    return 60

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
