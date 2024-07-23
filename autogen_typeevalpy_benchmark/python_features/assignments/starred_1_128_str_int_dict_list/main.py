# Functions are assigned to variables via starred assignment
def func1():
    return 'yayqp'


def func2():
    return 58


def func3():
    return {'nkfrl': 96, 'lfnmz': 98, 'ycqfm': 92}


def func4():
    return [41, 9, 26]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
