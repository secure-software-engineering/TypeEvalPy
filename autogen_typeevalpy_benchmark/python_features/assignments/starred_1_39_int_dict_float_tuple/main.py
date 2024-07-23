# Functions are assigned to variables via starred assignment
def func1():
    return 85


def func2():
    return {'bggtn': 6, 'ozoth': 92, 'rsxlj': 68}


def func3():
    return 34.35


def func4():
    return (70, 88, 40)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
