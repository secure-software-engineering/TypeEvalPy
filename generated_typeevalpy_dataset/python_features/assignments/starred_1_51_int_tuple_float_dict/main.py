# Functions are assigned to variables via starred assignment
def func1():
    return 2


def func2():
    return (49, 21, 73)


def func3():
    return 82.53


def func4():
    return {'fuvzy': 67, 'ahmdu': 79, 'xhrfe': 8}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
