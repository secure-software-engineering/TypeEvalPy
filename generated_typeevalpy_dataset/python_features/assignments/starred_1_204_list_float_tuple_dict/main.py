# Functions are assigned to variables via starred assignment
def func1():
    return [85, 33, 20]


def func2():
    return 79.25


def func3():
    return (3, 36, 17)


def func4():
    return {'rllkj': 69, 'ewxyx': 18, 'tauev': 19}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
