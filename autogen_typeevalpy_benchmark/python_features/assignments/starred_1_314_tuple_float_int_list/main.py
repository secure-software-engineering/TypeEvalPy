# Functions are assigned to variables via starred assignment
def func1():
    return (69, 100, 63)


def func2():
    return 30.02


def func3():
    return 90


def func4():
    return [70, 89, 68]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
