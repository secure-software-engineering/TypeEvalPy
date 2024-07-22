# Functions are assigned to variables via starred assignment
def func1():
    return 85


def func2():
    return (1, 82, 27)


def func3():
    return 53.92


def func4():
    return [54, 96, 88]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
