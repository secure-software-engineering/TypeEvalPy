# Functions are assigned to variables via starred assignment
def func1():
    return 75


def func2():
    return 79.97


def func3():
    return (91, 37, 15)


def func4():
    return [27, 87, 56]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
