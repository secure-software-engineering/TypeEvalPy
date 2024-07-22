# Functions are assigned to variables via starred assignment
def func1():
    return 23.04


def func2():
    return 'hxtag'


def func3():
    return {'qqecy': 77, 'jsgkt': 86, 'fijiy': 41}


def func4():
    return 45

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
