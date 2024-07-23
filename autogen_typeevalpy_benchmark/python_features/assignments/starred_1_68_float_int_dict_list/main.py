# Functions are assigned to variables via starred assignment
def func1():
    return 36.33


def func2():
    return 4


def func3():
    return {'ccmqz': 18, 'mwzrk': 46, 'jakgp': 99}


def func4():
    return [32, 84, 65]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
