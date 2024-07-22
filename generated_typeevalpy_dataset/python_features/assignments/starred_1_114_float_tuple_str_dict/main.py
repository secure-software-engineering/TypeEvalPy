# Functions are assigned to variables via starred assignment
def func1():
    return 37.17


def func2():
    return (80, 25, 91)


def func3():
    return 'yxgvd'


def func4():
    return {'fcykz': 12, 'gboyw': 74, 'bcwde': 98}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
