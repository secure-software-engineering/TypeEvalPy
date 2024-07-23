# Functions are assigned to variables via starred assignment
def func1():
    return {'gpjcj': 88, 'kjuuk': 77, 'zfxgg': 41}


def func2():
    return (48, 89, 69)


def func3():
    return 4


def func4():
    return [43, 5, 10]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
