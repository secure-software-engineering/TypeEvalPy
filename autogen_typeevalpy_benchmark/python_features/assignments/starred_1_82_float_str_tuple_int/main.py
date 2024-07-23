# Functions are assigned to variables via starred assignment
def func1():
    return 59.99


def func2():
    return 'gymvr'


def func3():
    return (85, 96, 13)


def func4():
    return 95

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
