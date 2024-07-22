# Functions are assigned to variables via starred assignment
def func1():
    return (99, 38, 80)


def func2():
    return 88.36


def func3():
    return 16


def func4():
    return {'heano': 79, 'rplzx': 91, 'lhnvd': 19}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
