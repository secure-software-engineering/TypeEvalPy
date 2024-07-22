# Functions are assigned to variables via starred assignment
def func1():
    return 76


def func2():
    return 4.29


def func3():
    return (69, 35, 67)


def func4():
    return {'uqzoa': 10, 'qbayj': 100, 'yyjoz': 65}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
