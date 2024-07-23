# Functions are assigned to variables via starred assignment
def func1():
    return [72, 35, 3]


def func2():
    return 55


def func3():
    return 11.14


def func4():
    return (98, 32, 22)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
