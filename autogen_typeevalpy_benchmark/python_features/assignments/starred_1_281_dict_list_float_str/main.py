# Functions are assigned to variables via starred assignment
def func1():
    return {'lwczu': 46, 'syrou': 70, 'ykiwx': 54}


def func2():
    return [64, 64, 73]


def func3():
    return 17.65


def func4():
    return 'zywld'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
