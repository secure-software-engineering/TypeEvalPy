# Functions are assigned to variables via starred assignment
def func1():
    return 96.97


def func2():
    return (47, 10, 65)


def func3():
    return [87, 25, 2]


def func4():
    return 19

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
