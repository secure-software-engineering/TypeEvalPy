# Functions are assigned to variables via starred assignment
def func1():
    return 13.97


def func2():
    return 'pbrfy'


def func3():
    return (79, 94, 63)


def func4():
    return [21, 94, 90]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
