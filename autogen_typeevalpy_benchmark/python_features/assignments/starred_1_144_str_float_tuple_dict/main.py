# Functions are assigned to variables via starred assignment
def func1():
    return 'qraah'


def func2():
    return 85.95


def func3():
    return (18, 82, 100)


def func4():
    return {'xphck': 75, 'ueapg': 85, 'cpqdz': 97}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
