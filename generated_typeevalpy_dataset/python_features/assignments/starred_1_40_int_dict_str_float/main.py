# Functions are assigned to variables via starred assignment
def func1():
    return 66


def func2():
    return {'xgavt': 34, 'kvqvl': 88, 'hfifh': 17}


def func3():
    return 'ottly'


def func4():
    return 99.77

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
