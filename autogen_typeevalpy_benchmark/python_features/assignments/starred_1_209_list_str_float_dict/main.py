# Functions are assigned to variables via starred assignment
def func1():
    return [46, 86, 84]


def func2():
    return 'klwhr'


def func3():
    return 69.58


def func4():
    return {'kxntp': 65, 'cchtt': 72, 'wtpmn': 13}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
