# Functions are assigned to variables via starred assignment
def func1():
    return {'qtxxq': 61, 'egalr': 6, 'mfdje': 72}


def func2():
    return [84, 3, 37]


def func3():
    return (11, 13, 18)


def func4():
    return 56

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
