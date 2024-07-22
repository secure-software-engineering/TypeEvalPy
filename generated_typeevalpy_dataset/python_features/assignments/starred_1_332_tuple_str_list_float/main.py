# Functions are assigned to variables via starred assignment
def func1():
    return (2, 44, 74)


def func2():
    return 'cvnvt'


def func3():
    return [22, 13, 51]


def func4():
    return 51.6

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
