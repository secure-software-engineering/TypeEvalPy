# Functions are assigned to variables via starred assignment
def func1():
    return (2, 37, 45)


def func2():
    return {'tvsky': 92, 'vgmfy': 42, 'globu': 17}


def func3():
    return 'norki'


def func4():
    return 12

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
