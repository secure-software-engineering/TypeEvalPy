# Functions are assigned to variables via starred assignment
def func1():
    return 14.47


def func2():
    return [62, 85, 29]


def func3():
    return 91


def func4():
    return {'haxhq': 32, 'qtycq': 24, 'wvfvk': 94}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
