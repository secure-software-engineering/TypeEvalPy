# Functions are assigned to variables via starred assignment
def func1():
    return {'kpxrl': 43, 'monot': 81, 'kxvww': 53}


def func2():
    return 82.35


def func3():
    return 'kipop'


def func4():
    return (18, 97, 24)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
