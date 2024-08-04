# Functions are assigned to variables via starred assignment
def func1():
    return [62, 69, 99]


def func2():
    return 44


def func3():
    return 'hoyea'


def func4():
    return {'znmxr': 63, 'fnqlu': 10, 'wizdd': 35}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
