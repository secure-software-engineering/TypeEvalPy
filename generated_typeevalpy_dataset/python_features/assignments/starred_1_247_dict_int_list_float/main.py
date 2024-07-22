# Functions are assigned to variables via starred assignment
def func1():
    return {'nmvrf': 3, 'eieal': 12, 'uxueo': 31}


def func2():
    return 19


def func3():
    return [65, 42, 84]


def func4():
    return 84.72

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
