# Functions are assigned to variables via starred assignment
def func1():
    return (35, 33, 11)


def func2():
    return 37.62


def func3():
    return [23, 70, 15]


def func4():
    return 'sssxb'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
