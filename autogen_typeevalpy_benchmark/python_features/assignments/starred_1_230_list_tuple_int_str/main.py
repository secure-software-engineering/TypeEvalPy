# Functions are assigned to variables via starred assignment
def func1():
    return [10, 60, 39]


def func2():
    return (3, 87, 51)


def func3():
    return 38


def func4():
    return 'rayly'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
