# Functions are assigned to variables via starred assignment
def func1():
    return [19, 21, 34]


def func2():
    return {'sdnve': 90, 'bwgbj': 20, 'fbvcn': 49}


def func3():
    return 68.22


def func4():
    return 'qvxup'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
