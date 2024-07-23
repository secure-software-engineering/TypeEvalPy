# Functions are assigned to variables via starred assignment
def func1():
    return [29, 1, 78]


def func2():
    return (70, 57, 76)


def func3():
    return 'hmolr'


def func4():
    return 41.04

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
