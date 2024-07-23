# Functions are assigned to variables via starred assignment
def func1():
    return 'rgnse'


def func2():
    return [75, 1, 67]


def func3():
    return {'oywqx': 96, 'syohs': 3, 'kpoai': 23}


def func4():
    return (50, 54, 100)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
