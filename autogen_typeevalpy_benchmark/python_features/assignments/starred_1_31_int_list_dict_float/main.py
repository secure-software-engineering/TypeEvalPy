# Functions are assigned to variables via starred assignment
def func1():
    return 1


def func2():
    return [40, 69, 6]


def func3():
    return {'eqyiy': 57, 'boytq': 54, 'btbgf': 55}


def func4():
    return 9.76

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
