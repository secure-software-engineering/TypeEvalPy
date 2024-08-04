# Functions are assigned to variables via starred assignment
def func1():
    return 'lpgsx'


def func2():
    return 5.93


def func3():
    return [27, 45, 95]


def func4():
    return (65, 24, 8)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
