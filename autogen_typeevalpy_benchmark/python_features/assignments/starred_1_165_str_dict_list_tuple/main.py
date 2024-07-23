# Functions are assigned to variables via starred assignment
def func1():
    return 'hrles'


def func2():
    return {'talna': 67, 'zmhxm': 19, 'kgekd': 52}


def func3():
    return [16, 32, 83]


def func4():
    return (16, 77, 75)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
