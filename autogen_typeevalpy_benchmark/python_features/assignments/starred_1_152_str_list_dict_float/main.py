# Functions are assigned to variables via starred assignment
def func1():
    return 'iqdyw'


def func2():
    return [69, 25, 6]


def func3():
    return {'drzuq': 56, 'nkwaj': 73, 'gwrjs': 32}


def func4():
    return 86.35

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
