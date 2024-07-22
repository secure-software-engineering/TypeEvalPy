# Functions are assigned to variables via starred assignment
def func1():
    return {'bbxuw': 85, 'iydto': 95, 'snsgs': 3}


def func2():
    return (59, 59, 90)


def func3():
    return 22


def func4():
    return 81.5

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
