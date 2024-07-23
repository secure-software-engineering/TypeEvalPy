# Functions are assigned to variables via starred assignment
def func1():
    return (62, 82, 90)


def func2():
    return 39


def func3():
    return 61.94


def func4():
    return [39, 45, 36]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
