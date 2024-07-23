# Functions are assigned to variables via starred assignment
def func1():
    return (95, 48, 11)


def func2():
    return {'mbdyo': 72, 'bzcsu': 83, 'exknr': 82}


def func3():
    return 75


def func4():
    return 37.99

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
