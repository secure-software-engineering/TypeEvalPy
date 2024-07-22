# Functions are assigned to variables via starred assignment
def func1():
    return [65, 48, 73]


def func2():
    return 24.58


def func3():
    return 16


def func4():
    return (37, 64, 66)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
