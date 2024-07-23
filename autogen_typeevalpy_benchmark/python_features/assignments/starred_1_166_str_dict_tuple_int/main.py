# Functions are assigned to variables via starred assignment
def func1():
    return 'vsbpz'


def func2():
    return {'jeiua': 83, 'lctnv': 18, 'xkiwl': 40}


def func3():
    return (29, 39, 62)


def func4():
    return 71

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
