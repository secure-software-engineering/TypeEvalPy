# Functions are assigned to variables via starred assignment
def func1():
    return {'rbmfk': 72, 'xasly': 38, 'kqwce': 94}


def func2():
    return 21


def func3():
    return 'faabk'


def func4():
    return (32, 5, 96)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
