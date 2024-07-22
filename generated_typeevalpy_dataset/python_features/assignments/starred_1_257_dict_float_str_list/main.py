# Functions are assigned to variables via starred assignment
def func1():
    return {'gpell': 16, 'kbpts': 9, 'wvtla': 6}


def func2():
    return 84.1


def func3():
    return 'rklyp'


def func4():
    return [6, 25, 23]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
