# Functions are assigned to variables via starred assignment
def func1():
    return 61


def func2():
    return {'qigft': 76, 'vflec': 25, 'gveep': 99}


def func3():
    return [49, 28, 17]


def func4():
    return (83, 23, 77)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
