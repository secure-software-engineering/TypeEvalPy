# Functions are assigned to variables via starred assignment
def func1():
    return (59, 47, 39)


def func2():
    return 'etwmy'


def func3():
    return {'vrxwt': 61, 'zemsm': 72, 'hrzma': 72}


def func4():
    return 16

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
