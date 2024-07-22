# Functions are assigned to variables via starred assignment
def func1():
    return [63, 77, 52]


def func2():
    return 24.93


def func3():
    return 'suiut'


def func4():
    return {'ysakw': 96, 'tjmyl': 43, 'pjjeo': 74}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
