# Functions are assigned to variables via starred assignment
def func1():
    return 52


def func2():
    return {'yynyu': 62, 'gzjxd': 75, 'daggd': 84}


def func3():
    return 7.01


def func4():
    return (37, 55, 76)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
