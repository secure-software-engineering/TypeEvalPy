# Functions are assigned to variables via starred assignment
def func1():
    return {'mjhjx': 47, 'qsntt': 90, 'nhfen': 29}


def func2():
    return 76


def func3():
    return 'noyll'


def func4():
    return (89, 14, 55)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
