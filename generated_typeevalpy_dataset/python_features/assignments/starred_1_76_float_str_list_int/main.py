# Functions are assigned to variables via starred assignment
def func1():
    return 92.64


def func2():
    return 'vmoyz'


def func3():
    return [71, 42, 42]


def func4():
    return 51

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
