# Functions are assigned to variables via starred assignment
def func1():
    return 'rspen'


def func2():
    return 62.64


def func3():
    return [36, 69, 91]


def func4():
    return 59

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
