# Functions are assigned to variables via starred assignment
def func1():
    return {'wbnli': 74, 'sknub': 48, 'vqjzz': 82}


def func2():
    return 'bmnxw'


def func3():
    return (98, 98, 34)


def func4():
    return 18

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
