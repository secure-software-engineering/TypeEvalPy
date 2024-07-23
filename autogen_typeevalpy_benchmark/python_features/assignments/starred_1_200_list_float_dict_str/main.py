# Functions are assigned to variables via starred assignment
def func1():
    return [26, 34, 63]


def func2():
    return 66.95


def func3():
    return {'hhtbv': 93, 'pwvtu': 80, 'msbnz': 82}


def func4():
    return 'pfegl'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
