# Functions are assigned to variables via starred assignment
def func1():
    return {'vuyvu': 90, 'ivjbs': 57, 'iftfe': 31}


def func2():
    return 'anhkp'


def func3():
    return 8.7


def func4():
    return 92

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
