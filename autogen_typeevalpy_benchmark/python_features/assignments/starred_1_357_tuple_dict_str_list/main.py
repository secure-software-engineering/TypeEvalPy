# Functions are assigned to variables via starred assignment
def func1():
    return (87, 50, 36)


def func2():
    return {'kpqgf': 31, 'uggki': 65, 'zecja': 58}


def func3():
    return 'bnbii'


def func4():
    return [80, 38, 49]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
