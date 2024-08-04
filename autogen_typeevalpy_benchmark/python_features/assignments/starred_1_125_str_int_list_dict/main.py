# Functions are assigned to variables via starred assignment
def func1():
    return 'yafho'


def func2():
    return 91


def func3():
    return [12, 96, 1]


def func4():
    return {'aoduq': 85, 'yqmto': 60, 'lseay': 35}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
