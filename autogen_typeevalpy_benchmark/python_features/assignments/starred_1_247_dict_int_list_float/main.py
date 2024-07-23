# Functions are assigned to variables via starred assignment
def func1():
    return {'tweey': 93, 'pfmng': 29, 'fmvpb': 52}


def func2():
    return 78


def func3():
    return [97, 22, 82]


def func4():
    return 59.13

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
