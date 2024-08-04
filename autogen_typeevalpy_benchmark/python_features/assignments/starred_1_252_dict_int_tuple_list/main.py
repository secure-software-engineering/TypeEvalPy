# Functions are assigned to variables via starred assignment
def func1():
    return {'ckdyv': 91, 'eadcj': 54, 'iapup': 13}


def func2():
    return 94


def func3():
    return (93, 99, 25)


def func4():
    return [16, 43, 21]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
