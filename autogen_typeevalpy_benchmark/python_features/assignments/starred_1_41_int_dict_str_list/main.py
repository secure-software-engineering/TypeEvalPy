# Functions are assigned to variables via starred assignment
def func1():
    return 82


def func2():
    return {'ojxay': 47, 'qadge': 31, 'ksdso': 61}


def func3():
    return 'ythav'


def func4():
    return [64, 89, 12]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
