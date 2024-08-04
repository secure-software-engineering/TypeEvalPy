# Functions are assigned to variables via starred assignment
def func1():
    return 'uwgnv'


def func2():
    return (44, 37, 69)


def func3():
    return {'mygdp': 57, 'tuugj': 53, 'zxnag': 98}


def func4():
    return 39

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
