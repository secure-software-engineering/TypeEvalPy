# Functions are assigned to variables via starred assignment
def func1():
    return {'flezo': 69, 'ilrow': 9, 'emvxp': 96}


def func2():
    return 43.58


def func3():
    return (96, 48, 8)


def func4():
    return 77

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
