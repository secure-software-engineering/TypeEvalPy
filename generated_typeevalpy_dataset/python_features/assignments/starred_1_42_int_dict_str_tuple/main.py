# Functions are assigned to variables via starred assignment
def func1():
    return 26


def func2():
    return {'daxtq': 17, 'vqiiu': 11, 'csnfl': 5}


def func3():
    return 'elcma'


def func4():
    return (58, 47, 20)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
