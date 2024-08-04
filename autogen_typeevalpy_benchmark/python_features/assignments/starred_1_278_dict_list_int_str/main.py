# Functions are assigned to variables via starred assignment
def func1():
    return {'sryqw': 98, 'kptli': 95, 'vedrr': 34}


def func2():
    return [86, 84, 22]


def func3():
    return 8


def func4():
    return 'hkcuf'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
