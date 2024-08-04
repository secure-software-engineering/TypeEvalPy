# Functions are assigned to variables via starred assignment
def func1():
    return 61


def func2():
    return (24, 70, 14)


def func3():
    return 42.16


def func4():
    return [26, 32, 57]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
