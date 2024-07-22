# Functions are assigned to variables via starred assignment
def func1():
    return 31.49


def func2():
    return [38, 33, 25]


def func3():
    return 34


def func4():
    return {'edlcz': 25, 'tegqt': 14, 'olbyy': 39}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
