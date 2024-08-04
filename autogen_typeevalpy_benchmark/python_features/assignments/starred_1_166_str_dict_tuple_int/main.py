# Functions are assigned to variables via starred assignment
def func1():
    return 'usdwt'


def func2():
    return {'hxtdo': 78, 'eojyp': 59, 'mpyit': 13}


def func3():
    return (64, 64, 11)


def func4():
    return 63

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
