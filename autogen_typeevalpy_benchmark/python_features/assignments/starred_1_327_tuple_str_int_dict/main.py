# Functions are assigned to variables via starred assignment
def func1():
    return (18, 8, 23)


def func2():
    return 'ilfcn'


def func3():
    return 30


def func4():
    return {'rhxfb': 36, 'blljq': 95, 'eaulo': 52}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
