# Functions are assigned to variables via starred assignment
def func1():
    return (87, 46, 81)


def func2():
    return [48, 10, 15]


def func3():
    return 'uqavt'


def func4():
    return {'udmbk': 53, 'lvbfa': 55, 'pvpai': 94}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
