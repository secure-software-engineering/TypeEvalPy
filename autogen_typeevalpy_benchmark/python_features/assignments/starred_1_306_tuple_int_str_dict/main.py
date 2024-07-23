# Functions are assigned to variables via starred assignment
def func1():
    return (64, 44, 27)


def func2():
    return 65


def func3():
    return 'sxuej'


def func4():
    return {'hvgqu': 56, 'fljuq': 36, 'pgacu': 36}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
