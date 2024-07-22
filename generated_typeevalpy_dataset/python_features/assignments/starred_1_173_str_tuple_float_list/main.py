# Functions are assigned to variables via starred assignment
def func1():
    return 'qbpta'


def func2():
    return (17, 61, 37)


def func3():
    return 39.59


def func4():
    return [1, 44, 64]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
