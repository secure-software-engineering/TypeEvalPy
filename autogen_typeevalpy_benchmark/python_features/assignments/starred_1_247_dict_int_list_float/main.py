# Functions are assigned to variables via starred assignment
def func1():
    return {'yspeg': 26, 'qdmzv': 11, 'ecxrn': 22}


def func2():
    return 82


def func3():
    return [57, 30, 92]


def func4():
    return 43.25

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
