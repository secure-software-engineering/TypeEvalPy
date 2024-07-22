# Functions are assigned to variables via starred assignment
def func1():
    return 21


def func2():
    return [37, 69, 32]


def func3():
    return 'ubjae'


def func4():
    return (10, 27, 66)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
