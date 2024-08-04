# Functions are assigned to variables via starred assignment
def func1():
    return {'hbjgi': 15, 'oplej': 12, 'gdlpc': 89}


def func2():
    return [8, 90, 67]


def func3():
    return 37.82


def func4():
    return 'sbnkl'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
