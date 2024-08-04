# Functions are assigned to variables via starred assignment
def func1():
    return 68


def func2():
    return [86, 86, 46]


def func3():
    return (4, 12, 94)


def func4():
    return {'rwuey': 11, 'eelln': 51, 'rasfq': 42}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
