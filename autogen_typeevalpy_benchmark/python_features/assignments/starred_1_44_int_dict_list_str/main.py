# Functions are assigned to variables via starred assignment
def func1():
    return 85


def func2():
    return {'vmnan': 94, 'pguqu': 56, 'pfvgg': 77}


def func3():
    return [89, 44, 69]


def func4():
    return 'aashu'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
