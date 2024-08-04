# Functions are assigned to variables via starred assignment
def func1():
    return 98.22


def func2():
    return (23, 40, 21)


def func3():
    return {'cpjmv': 12, 'zwvtc': 38, 'bimfc': 93}


def func4():
    return 'kfcwj'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
