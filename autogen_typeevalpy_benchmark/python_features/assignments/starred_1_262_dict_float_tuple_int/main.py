# Functions are assigned to variables via starred assignment
def func1():
    return {'fnqij': 76, 'bxggs': 74, 'uvubn': 12}


def func2():
    return 98.54


def func3():
    return (5, 78, 39)


def func4():
    return 48

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
