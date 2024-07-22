# Functions are assigned to variables via starred assignment
def func1():
    return 73


def func2():
    return 'sxeqh'


def func3():
    return 21.3


def func4():
    return (64, 68, 39)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
