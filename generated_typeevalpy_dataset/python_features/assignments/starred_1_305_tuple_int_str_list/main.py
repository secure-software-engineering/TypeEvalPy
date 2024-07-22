# Functions are assigned to variables via starred assignment
def func1():
    return (31, 37, 43)


def func2():
    return 30


def func3():
    return 'dxnvk'


def func4():
    return [95, 80, 36]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
