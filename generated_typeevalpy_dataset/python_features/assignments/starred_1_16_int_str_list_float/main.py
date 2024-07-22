# Functions are assigned to variables via starred assignment
def func1():
    return 1


def func2():
    return 'ttjce'


def func3():
    return [69, 22, 91]


def func4():
    return 84.29

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
