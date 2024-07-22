# Functions are assigned to variables via starred assignment
def func1():
    return 81.07


def func2():
    return [11, 72, 38]


def func3():
    return 'mznyq'


def func4():
    return {'povnq': 63, 'wjndb': 40, 'sihce': 86}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
