# Functions are assigned to variables via starred assignment
def func1():
    return [5, 80, 56]


def func2():
    return 'rjtpr'


def func3():
    return 40


def func4():
    return {'rygqz': 49, 'gmpau': 40, 'oiymv': 31}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
