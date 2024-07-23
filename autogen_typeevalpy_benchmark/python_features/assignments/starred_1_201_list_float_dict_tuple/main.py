# Functions are assigned to variables via starred assignment
def func1():
    return [63, 85, 62]


def func2():
    return 50.11


def func3():
    return {'ynzos': 80, 'idhoe': 60, 'jeoyw': 11}


def func4():
    return (95, 95, 77)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
