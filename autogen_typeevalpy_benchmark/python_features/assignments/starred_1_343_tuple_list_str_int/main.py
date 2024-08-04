# Functions are assigned to variables via starred assignment
def func1():
    return (17, 44, 91)


def func2():
    return [72, 26, 62]


def func3():
    return 'tozbu'


def func4():
    return 27

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
