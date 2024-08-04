# Functions are assigned to variables via starred assignment
def func1():
    return [85, 67, 39]


def func2():
    return (85, 73, 94)


def func3():
    return 53


def func4():
    return 'zyjeo'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
