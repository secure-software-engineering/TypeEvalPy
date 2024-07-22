# Functions are assigned to variables via starred assignment
def func1():
    return [66, 72, 63]


def func2():
    return (46, 50, 57)


def func3():
    return 87.02


def func4():
    return 20

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
