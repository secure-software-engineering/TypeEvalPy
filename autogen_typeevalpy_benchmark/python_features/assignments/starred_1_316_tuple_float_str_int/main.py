# Functions are assigned to variables via starred assignment
def func1():
    return (42, 55, 66)


def func2():
    return 68.52


def func3():
    return 'fxsbk'


def func4():
    return 33

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
