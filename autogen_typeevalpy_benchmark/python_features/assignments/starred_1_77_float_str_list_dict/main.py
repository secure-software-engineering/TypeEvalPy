# Functions are assigned to variables via starred assignment
def func1():
    return 85.51


def func2():
    return 'uzjto'


def func3():
    return [69, 85, 14]


def func4():
    return {'zxacf': 47, 'uwwiw': 46, 'ckvel': 58}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
