# Functions are assigned to variables via starred assignment
def func1():
    return {'colrh': 64, 'nlvvf': 85, 'rreaz': 32}


def func2():
    return 'rjeme'


def func3():
    return 21


def func4():
    return 83.63

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
