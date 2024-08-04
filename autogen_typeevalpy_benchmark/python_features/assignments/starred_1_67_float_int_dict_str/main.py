# Functions are assigned to variables via starred assignment
def func1():
    return 18.85


def func2():
    return 59


def func3():
    return {'ajtwp': 15, 'cgqjy': 77, 'kmqik': 24}


def func4():
    return 'lmglr'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
