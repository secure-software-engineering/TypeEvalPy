# Functions are assigned to variables via starred assignment
def func1():
    return 67.18


def func2():
    return (82, 48, 75)


def func3():
    return 48


def func4():
    return 'hxxgo'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
