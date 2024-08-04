# Functions are assigned to variables via starred assignment
def func1():
    return 'pisaw'


def func2():
    return 82


def func3():
    return {'nsnlz': 66, 'gaxiv': 57, 'ldnmn': 94}


def func4():
    return [49, 45, 55]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
