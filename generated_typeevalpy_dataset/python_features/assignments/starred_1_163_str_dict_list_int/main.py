# Functions are assigned to variables via starred assignment
def func1():
    return 'bxeif'


def func2():
    return {'hzwip': 48, 'lwxsg': 53, 'fwxuk': 20}


def func3():
    return [82, 85, 43]


def func4():
    return 6

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
