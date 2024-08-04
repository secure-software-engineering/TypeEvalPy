# Functions are assigned to variables via starred assignment
def func1():
    return (46, 90, 52)


def func2():
    return [21, 99, 99]


def func3():
    return 'nmxvv'


def func4():
    return {'meipc': 33, 'gfmts': 5, 'xasir': 27}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
