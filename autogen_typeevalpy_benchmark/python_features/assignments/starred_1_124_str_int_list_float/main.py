# Functions are assigned to variables via starred assignment
def func1():
    return 'koain'


def func2():
    return 97


def func3():
    return [35, 91, 18]


def func4():
    return 72.23

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
