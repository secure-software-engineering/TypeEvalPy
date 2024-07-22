# Functions are assigned to variables via starred assignment
def func1():
    return 'wcwdq'


def func2():
    return [91, 48, 23]


def func3():
    return {'gmjpe': 70, 'gghzg': 98, 'epkpj': 33}


def func4():
    return (44, 96, 71)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
