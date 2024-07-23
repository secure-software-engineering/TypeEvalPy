# Functions are assigned to variables via starred assignment
def func1():
    return 'yvvsa'


def func2():
    return {'yqten': 13, 'odyoj': 5, 'pmxkg': 13}


def func3():
    return (62, 63, 89)


def func4():
    return 55.24

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
