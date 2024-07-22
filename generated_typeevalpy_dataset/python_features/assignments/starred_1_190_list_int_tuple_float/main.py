# Functions are assigned to variables via starred assignment
def func1():
    return [50, 64, 75]


def func2():
    return 6


def func3():
    return (70, 73, 73)


def func4():
    return 27.49

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
