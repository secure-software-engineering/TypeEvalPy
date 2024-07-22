# Functions are assigned to variables via starred assignment
def func1():
    return [67, 76, 17]


def func2():
    return 'nypit'


def func3():
    return {'avzpk': 9, 'cvhwc': 10, 'ctaqe': 90}


def func4():
    return 63

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
