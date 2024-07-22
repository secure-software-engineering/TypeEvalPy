# Functions are assigned to variables via starred assignment
def func1():
    return {'blchc': 18, 'cptse': 57, 'ezqpd': 71}


def func2():
    return (76, 62, 52)


def func3():
    return 82


def func4():
    return 'neegi'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
