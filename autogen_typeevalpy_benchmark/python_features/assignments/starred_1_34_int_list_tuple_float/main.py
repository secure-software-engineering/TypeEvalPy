# Functions are assigned to variables via starred assignment
def func1():
    return 97


def func2():
    return [94, 14, 52]


def func3():
    return (63, 55, 62)


def func4():
    return 69.32

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
