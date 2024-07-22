# Functions are assigned to variables via starred assignment
def func1():
    return 87


def func2():
    return 17.38


def func3():
    return [89, 67, 4]


def func4():
    return 'jbelu'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
