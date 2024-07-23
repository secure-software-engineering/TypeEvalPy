# Functions are assigned to variables via starred assignment
def func1():
    return 'nwghh'


def func2():
    return (3, 62, 82)


def func3():
    return {'qbdhv': 49, 'itauf': 87, 'yhbkf': 76}


def func4():
    return [22, 13, 64]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
