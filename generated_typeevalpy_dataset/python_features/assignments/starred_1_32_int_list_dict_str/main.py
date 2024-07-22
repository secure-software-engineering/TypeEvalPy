# Functions are assigned to variables via starred assignment
def func1():
    return 10


def func2():
    return [24, 25, 24]


def func3():
    return {'ibyid': 76, 'udpdr': 7, 'gazwa': 86}


def func4():
    return 'zomxs'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
