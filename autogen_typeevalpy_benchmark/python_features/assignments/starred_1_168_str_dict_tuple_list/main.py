# Functions are assigned to variables via starred assignment
def func1():
    return 'lwlbk'


def func2():
    return {'fiyvy': 75, 'ulqvv': 54, 'qmgfe': 96}


def func3():
    return (93, 93, 58)


def func4():
    return [43, 97, 64]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
