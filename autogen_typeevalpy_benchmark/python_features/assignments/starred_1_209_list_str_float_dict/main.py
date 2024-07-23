# Functions are assigned to variables via starred assignment
def func1():
    return [86, 66, 39]


def func2():
    return 'gdwla'


def func3():
    return 7.42


def func4():
    return {'rndkq': 62, 'pzdpl': 24, 'qqjpv': 28}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
