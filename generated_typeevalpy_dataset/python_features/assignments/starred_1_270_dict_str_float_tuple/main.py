# Functions are assigned to variables via starred assignment
def func1():
    return {'vmizg': 98, 'rmanq': 37, 'bjfyk': 93}


def func2():
    return 'rqdlg'


def func3():
    return 75.54


def func4():
    return (58, 55, 53)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
