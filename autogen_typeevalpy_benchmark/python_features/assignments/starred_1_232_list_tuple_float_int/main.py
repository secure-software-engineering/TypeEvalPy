# Functions are assigned to variables via starred assignment
def func1():
    return [14, 59, 28]


def func2():
    return (73, 39, 98)


def func3():
    return 43.33


def func4():
    return 20

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
