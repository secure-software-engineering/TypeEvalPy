# Functions are assigned to variables via starred assignment
def func1():
    return 96.08


def func2():
    return 'cwdng'


def func3():
    return [23, 6, 2]


def func4():
    return (8, 89, 98)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
