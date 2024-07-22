# Functions are assigned to variables via starred assignment
def func1():
    return [85, 4, 50]


def func2():
    return 74


def func3():
    return 'wkqhn'


def func4():
    return {'krjps': 5, 'jesyz': 56, 'oadye': 14}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
