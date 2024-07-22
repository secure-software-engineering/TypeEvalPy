# Functions are assigned to variables via starred assignment
def func1():
    return 63.3


def func2():
    return 10


def func3():
    return (5, 18, 47)


def func4():
    return 'anekg'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
