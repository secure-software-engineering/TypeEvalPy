# Functions are assigned to variables via starred assignment
def func1():
    return 87.09


def func2():
    return [51, 16, 40]


def func3():
    return {'yvcqu': 18, 'zqjld': 6, 'pvxpc': 94}


def func4():
    return 41

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
