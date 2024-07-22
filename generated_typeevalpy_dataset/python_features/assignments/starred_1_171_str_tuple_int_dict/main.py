# Functions are assigned to variables via starred assignment
def func1():
    return 'hppga'


def func2():
    return (97, 51, 17)


def func3():
    return 36


def func4():
    return {'fmvfq': 52, 'yjpel': 68, 'bfeco': 32}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
