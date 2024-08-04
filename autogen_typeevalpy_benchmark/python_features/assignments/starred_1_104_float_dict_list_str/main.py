# Functions are assigned to variables via starred assignment
def func1():
    return 89.13


def func2():
    return {'kylib': 37, 'pxxpv': 84, 'gmujh': 31}


def func3():
    return [37, 65, 92]


def func4():
    return 'ipwll'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
