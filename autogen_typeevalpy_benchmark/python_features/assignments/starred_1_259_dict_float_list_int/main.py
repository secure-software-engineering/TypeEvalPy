# Functions are assigned to variables via starred assignment
def func1():
    return {'rtwrw': 31, 'djqyw': 74, 'nncug': 60}


def func2():
    return 40.2


def func3():
    return [32, 7, 92]


def func4():
    return 73

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
