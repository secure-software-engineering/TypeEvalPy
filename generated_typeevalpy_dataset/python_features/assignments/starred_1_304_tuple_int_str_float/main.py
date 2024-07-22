# Functions are assigned to variables via starred assignment
def func1():
    return (40, 37, 60)


def func2():
    return 52


def func3():
    return 'cdncv'


def func4():
    return 24.65

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
