# Functions are assigned to variables via starred assignment
def func1():
    return 93.57


def func2():
    return {'vikoa': 26, 'vyhwg': 28, 'ewoag': 55}


def func3():
    return 79


def func4():
    return (70, 6, 67)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
