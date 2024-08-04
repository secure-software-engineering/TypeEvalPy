# Functions are assigned to variables via starred assignment
def func1():
    return (97, 75, 29)


def func2():
    return [22, 5, 64]


def func3():
    return 97


def func4():
    return 70.92

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
