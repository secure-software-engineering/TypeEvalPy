# Functions are assigned to variables via starred assignment
def func1():
    return {'ikudh': 23, 'wncwv': 33, 'zdwue': 37}


def func2():
    return 57.96


def func3():
    return 49


def func4():
    return 'ueffc'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
