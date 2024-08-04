# Functions are assigned to variables via starred assignment
def func1():
    return 35.17


def func2():
    return (80, 23, 28)


def func3():
    return {'nycfn': 34, 'ycxtt': 17, 'zybgk': 91}


def func4():
    return 78

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
