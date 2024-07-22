# Functions are assigned to variables via starred assignment
def func1():
    return {'aiovu': 84, 'ryucz': 7, 'argmk': 67}


def func2():
    return 'iqcoz'


def func3():
    return 98


def func4():
    return (59, 6, 87)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
