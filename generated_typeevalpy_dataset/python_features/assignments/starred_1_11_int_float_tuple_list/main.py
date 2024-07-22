# Functions are assigned to variables via starred assignment
def func1():
    return 3


def func2():
    return 52.0


def func3():
    return (11, 97, 58)


def func4():
    return [49, 32, 90]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
