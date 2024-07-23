# Functions are assigned to variables via starred assignment
def func1():
    return 'xzmtq'


def func2():
    return 93.0


def func3():
    return [45, 36, 55]


def func4():
    return {'xvghk': 39, 'clqwb': 45, 'qtbqr': 24}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
