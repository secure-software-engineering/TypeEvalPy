# Functions are assigned to variables via starred assignment
def func1():
    return (32, 17, 65)


def func2():
    return [23, 21, 24]


def func3():
    return 'zzsji'


def func4():
    return 95

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
