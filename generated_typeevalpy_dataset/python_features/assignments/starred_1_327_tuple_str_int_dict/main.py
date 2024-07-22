# Functions are assigned to variables via starred assignment
def func1():
    return (18, 72, 24)


def func2():
    return 'nzjkh'


def func3():
    return 20


def func4():
    return {'bwpnr': 84, 'rwzaw': 52, 'pdgey': 20}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
