# Functions are assigned to variables via starred assignment
def func1():
    return 6


def func2():
    return (87, 19, 71)


def func3():
    return [23, 93, 31]


def func4():
    return 11.6

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
