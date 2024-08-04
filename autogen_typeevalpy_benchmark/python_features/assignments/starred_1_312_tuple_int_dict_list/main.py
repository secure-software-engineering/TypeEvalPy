# Functions are assigned to variables via starred assignment
def func1():
    return (45, 77, 78)


def func2():
    return 36


def func3():
    return {'kpvkr': 4, 'gszgr': 75, 'bmtiv': 64}


def func4():
    return [9, 36, 84]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
