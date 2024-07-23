# Functions are assigned to variables via starred assignment
def func1():
    return 66


def func2():
    return (62, 31, 71)


def func3():
    return 40.09


def func4():
    return {'vmjga': 62, 'zbrlr': 37, 'xbife': 6}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
