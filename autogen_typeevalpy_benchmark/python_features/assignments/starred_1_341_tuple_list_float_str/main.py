# Functions are assigned to variables via starred assignment
def func1():
    return (20, 8, 24)


def func2():
    return [56, 23, 51]


def func3():
    return 61.53


def func4():
    return 'zbdtr'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
