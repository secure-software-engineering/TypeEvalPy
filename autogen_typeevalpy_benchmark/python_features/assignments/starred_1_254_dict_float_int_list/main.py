# Functions are assigned to variables via starred assignment
def func1():
    return {'bisaf': 65, 'kursb': 6, 'eblze': 63}


def func2():
    return 89.33


def func3():
    return 90


def func4():
    return [30, 53, 19]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
