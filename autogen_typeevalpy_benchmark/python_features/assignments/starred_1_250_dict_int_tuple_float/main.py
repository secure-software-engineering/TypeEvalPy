# Functions are assigned to variables via starred assignment
def func1():
    return {'naxrr': 4, 'wqflu': 78, 'oztdy': 15}


def func2():
    return 54


def func3():
    return (91, 51, 29)


def func4():
    return 13.27

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
