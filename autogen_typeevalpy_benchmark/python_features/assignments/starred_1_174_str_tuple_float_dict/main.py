# Functions are assigned to variables via starred assignment
def func1():
    return 'skfdk'


def func2():
    return (71, 61, 5)


def func3():
    return 62.85


def func4():
    return {'wwxlj': 57, 'broxk': 9, 'jmpwv': 86}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
