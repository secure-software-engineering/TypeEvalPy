# Functions are assigned to variables via starred assignment
def func1():
    return [56, 64, 78]


def func2():
    return 62


def func3():
    return {'radbd': 74, 'doosd': 83, 'fdovv': 26}


def func4():
    return 75.64

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
