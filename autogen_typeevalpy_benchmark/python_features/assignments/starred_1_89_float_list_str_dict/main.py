# Functions are assigned to variables via starred assignment
def func1():
    return 32.35


def func2():
    return [40, 10, 53]


def func3():
    return 'wzheo'


def func4():
    return {'iitdz': 94, 'tbcbs': 1, 'ocofb': 48}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
