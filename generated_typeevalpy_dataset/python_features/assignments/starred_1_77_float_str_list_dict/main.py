# Functions are assigned to variables via starred assignment
def func1():
    return 47.6


def func2():
    return 'qzphc'


def func3():
    return [83, 44, 36]


def func4():
    return {'ypfem': 89, 'ktcyo': 95, 'srshj': 61}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
