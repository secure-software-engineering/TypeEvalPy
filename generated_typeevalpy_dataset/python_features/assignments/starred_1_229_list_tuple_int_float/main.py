# Functions are assigned to variables via starred assignment
def func1():
    return [82, 18, 97]


def func2():
    return (43, 2, 65)


def func3():
    return 86


def func4():
    return 56.16

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
