# Functions are assigned to variables via starred assignment
def func1():
    return (32, 89, 29)


def func2():
    return [97, 87, 92]


def func3():
    return 72.77


def func4():
    return 'rsfxk'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
