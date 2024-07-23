# Functions are assigned to variables via starred assignment
def func1():
    return 'drvwd'


def func2():
    return 6.51


def func3():
    return 32


def func4():
    return (75, 64, 87)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
