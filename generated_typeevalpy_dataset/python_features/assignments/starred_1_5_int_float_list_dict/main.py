# Functions are assigned to variables via starred assignment
def func1():
    return 61


def func2():
    return 26.28


def func3():
    return [47, 97, 12]


def func4():
    return {'sbsob': 21, 'jpedp': 91, 'qskmb': 51}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
