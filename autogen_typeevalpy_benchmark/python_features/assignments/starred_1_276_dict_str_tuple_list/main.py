# Functions are assigned to variables via starred assignment
def func1():
    return {'qsbvb': 7, 'flojl': 42, 'jsqhc': 9}


def func2():
    return 'cyoar'


def func3():
    return (7, 14, 64)


def func4():
    return [72, 95, 47]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
