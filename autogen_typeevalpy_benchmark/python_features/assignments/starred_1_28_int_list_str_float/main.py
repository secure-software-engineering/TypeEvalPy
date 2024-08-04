# Functions are assigned to variables via starred assignment
def func1():
    return 38


def func2():
    return [1, 6, 5]


def func3():
    return 'rtrak'


def func4():
    return 5.91

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
