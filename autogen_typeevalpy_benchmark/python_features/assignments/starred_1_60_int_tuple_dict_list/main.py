# Functions are assigned to variables via starred assignment
def func1():
    return 41


def func2():
    return (7, 2, 23)


def func3():
    return {'aujug': 51, 'mpxti': 7, 'jbpnl': 31}


def func4():
    return [84, 100, 7]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
