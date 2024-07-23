# Functions are assigned to variables via starred assignment
def func1():
    return 66


def func2():
    return 95.97


def func3():
    return {'fnjot': 64, 'jzzkc': 94, 'jeagf': 46}


def func4():
    return [94, 7, 39]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
