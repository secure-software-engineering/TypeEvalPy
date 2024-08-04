# Functions are assigned to variables via starred assignment
def func1():
    return 'ublgj'


def func2():
    return (17, 71, 77)


def func3():
    return [54, 23, 24]


def func4():
    return 85

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
