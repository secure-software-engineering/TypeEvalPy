# Functions are assigned to variables via starred assignment
def func1():
    return 72.62


def func2():
    return 'itxjg'


def func3():
    return (43, 58, 41)


def func4():
    return {'ffwxg': 59, 'hbbeh': 52, 'jltcu': 75}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
