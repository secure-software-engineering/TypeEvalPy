# Functions are assigned to variables via starred assignment
def func1():
    return {'yitsf': 16, 'tzyrk': 37, 'fliri': 80}


def func2():
    return 45.6


def func3():
    return (34, 77, 89)


def func4():
    return [7, 25, 18]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
