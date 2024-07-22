# Functions are assigned to variables via starred assignment
def func1():
    return 57


def func2():
    return {'brnjt': 33, 'ivezm': 68, 'enpfm': 30}


def func3():
    return [95, 33, 66]


def func4():
    return 'hzoww'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
