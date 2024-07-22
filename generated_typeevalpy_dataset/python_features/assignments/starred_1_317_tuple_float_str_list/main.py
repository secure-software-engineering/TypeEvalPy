# Functions are assigned to variables via starred assignment
def func1():
    return (69, 51, 73)


def func2():
    return 42.67


def func3():
    return 'nzwhy'


def func4():
    return [63, 15, 22]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
