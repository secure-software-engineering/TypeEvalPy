# Functions are assigned to variables via starred assignment
def func1():
    return (34, 96, 95)


def func2():
    return 52


def func3():
    return {'hobwd': 17, 'uucrt': 10, 'zcqvm': 45}


def func4():
    return 'etgos'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
