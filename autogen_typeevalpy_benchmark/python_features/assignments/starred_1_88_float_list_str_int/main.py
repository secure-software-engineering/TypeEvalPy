# Functions are assigned to variables via starred assignment
def func1():
    return 79.3


def func2():
    return [38, 35, 22]


def func3():
    return 'hzwhr'


def func4():
    return 86

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
