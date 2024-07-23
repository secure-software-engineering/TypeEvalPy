# Functions are assigned to variables via starred assignment
def func1():
    return 77.67


def func2():
    return 3


def func3():
    return 'bbscn'


def func4():
    return [63, 13, 17]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
