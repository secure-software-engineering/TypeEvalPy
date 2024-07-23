# Functions are assigned to variables via starred assignment
def func1():
    return 19.82


def func2():
    return {'zmxtz': 67, 'qzygr': 63, 'tmkep': 18}


def func3():
    return 'tyzsm'


def func4():
    return [61, 74, 32]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
