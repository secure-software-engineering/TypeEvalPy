# Functions are assigned to variables via starred assignment
def func1():
    return [59, 97, 24]


def func2():
    return 30.32


def func3():
    return 'qmutd'


def func4():
    return 30

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
