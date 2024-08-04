# Functions are assigned to variables via starred assignment
def func1():
    return (46, 66, 39)


def func2():
    return 1.48


def func3():
    return [14, 15, 96]


def func4():
    return 100

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
