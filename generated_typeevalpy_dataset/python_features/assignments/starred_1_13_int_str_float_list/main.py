# Functions are assigned to variables via starred assignment
def func1():
    return 37


def func2():
    return 'rueyl'


def func3():
    return 34.84


def func4():
    return [90, 55, 12]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
