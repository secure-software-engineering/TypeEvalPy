# Functions are assigned to variables via starred assignment
def func1():
    return {'kizma': 13, 'rzwdy': 53, 'kahwn': 3}


def func2():
    return 64


def func3():
    return 'cyawi'


def func4():
    return [41, 59, 2]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
