# Functions are assigned to variables via starred assignment
def func1():
    return [57, 45, 93]


def func2():
    return {'jikpj': 69, 'beojo': 24, 'uvjwi': 27}


def func3():
    return (46, 20, 95)


def func4():
    return 77

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
