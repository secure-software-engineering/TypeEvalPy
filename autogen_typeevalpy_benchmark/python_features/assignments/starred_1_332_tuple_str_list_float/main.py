# Functions are assigned to variables via starred assignment
def func1():
    return (58, 1, 98)


def func2():
    return 'kwtqt'


def func3():
    return [84, 35, 85]


def func4():
    return 32.32

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
