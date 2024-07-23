# Functions are assigned to variables via starred assignment
def func1():
    return 'ynasy'


def func2():
    return {'tunxc': 47, 'lngix': 15, 'kdsrq': 51}


def func3():
    return [56, 2, 6]


def func4():
    return 49

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
