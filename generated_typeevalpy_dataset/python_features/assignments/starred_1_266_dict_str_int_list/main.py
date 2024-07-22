# Functions are assigned to variables via starred assignment
def func1():
    return {'cfyvi': 34, 'wejvl': 61, 'ubpht': 3}


def func2():
    return 'jfrki'


def func3():
    return 81


def func4():
    return [50, 62, 66]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
