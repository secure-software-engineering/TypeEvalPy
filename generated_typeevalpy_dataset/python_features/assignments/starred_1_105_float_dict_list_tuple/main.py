# Functions are assigned to variables via starred assignment
def func1():
    return 27.59


def func2():
    return {'qtzjp': 77, 'vzopz': 37, 'erbgo': 99}


def func3():
    return [49, 56, 36]


def func4():
    return (28, 70, 40)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
