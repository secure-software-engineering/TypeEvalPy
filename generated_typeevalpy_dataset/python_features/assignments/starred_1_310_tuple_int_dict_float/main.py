# Functions are assigned to variables via starred assignment
def func1():
    return (100, 23, 64)


def func2():
    return 22


def func3():
    return {'qdqml': 27, 'rqffk': 37, 'xmoif': 75}


def func4():
    return 96.66

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
