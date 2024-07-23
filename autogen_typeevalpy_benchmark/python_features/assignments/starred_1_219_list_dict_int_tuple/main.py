# Functions are assigned to variables via starred assignment
def func1():
    return [24, 45, 7]


def func2():
    return {'wetzb': 38, 'alwnc': 5, 'cxsno': 83}


def func3():
    return 79


def func4():
    return (23, 80, 97)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
