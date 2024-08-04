# Functions are assigned to variables via starred assignment
def func1():
    return 91.55


def func2():
    return (9, 33, 8)


def func3():
    return 'jfcka'


def func4():
    return 63

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
