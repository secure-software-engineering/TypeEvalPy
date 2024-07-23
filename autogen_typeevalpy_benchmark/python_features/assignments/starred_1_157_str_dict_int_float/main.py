# Functions are assigned to variables via starred assignment
def func1():
    return 'rkkcb'


def func2():
    return {'dklzf': 68, 'wgruv': 33, 'hwycu': 55}


def func3():
    return 79


def func4():
    return 21.94

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
