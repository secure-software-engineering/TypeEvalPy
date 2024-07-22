# Functions are assigned to variables via starred assignment
def func1():
    return 'rwrfa'


def func2():
    return [71, 89, 69]


def func3():
    return 20


def func4():
    return 68.68

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
