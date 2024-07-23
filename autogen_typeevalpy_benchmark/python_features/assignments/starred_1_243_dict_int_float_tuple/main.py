# Functions are assigned to variables via starred assignment
def func1():
    return {'gvniy': 23, 'efrgt': 66, 'emvew': 23}


def func2():
    return 87


def func3():
    return 34.87


def func4():
    return (56, 36, 27)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
