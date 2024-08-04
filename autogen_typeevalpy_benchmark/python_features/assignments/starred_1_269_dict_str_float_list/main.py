# Functions are assigned to variables via starred assignment
def func1():
    return {'uaqxa': 61, 'syreb': 21, 'pfial': 15}


def func2():
    return 'jsofg'


def func3():
    return 68.94


def func4():
    return [30, 76, 95]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
