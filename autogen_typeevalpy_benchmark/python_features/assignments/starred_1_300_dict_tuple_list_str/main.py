# Functions are assigned to variables via starred assignment
def func1():
    return {'ehxms': 66, 'ibfur': 94, 'mkqgf': 100}


def func2():
    return (71, 19, 39)


def func3():
    return [8, 25, 94]


def func4():
    return 'jweyu'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
