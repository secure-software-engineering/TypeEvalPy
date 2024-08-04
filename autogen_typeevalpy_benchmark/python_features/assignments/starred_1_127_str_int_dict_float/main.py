# Functions are assigned to variables via starred assignment
def func1():
    return 'ixviz'


def func2():
    return 83


def func3():
    return {'ayxyk': 34, 'uboey': 58, 'eauwx': 52}


def func4():
    return 69.57

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
